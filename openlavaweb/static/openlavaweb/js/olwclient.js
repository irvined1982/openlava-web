/*
     Copyright 2011 David Irvine

     This file is part of Openlava Web

     Openlava Web is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation, either version 3 of the License, or (at
     your option) any later version.

     Openlava Web is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
     General Public License for more details.

     You should have received a copy of the GNU General Public License
     along with Openlava Web. If not, see <http://www.gnu.org/licenses/>.

*/

var olwclient = olwclient || {};

olwclient.serverUrl = null;

olwclient.handleJSONResponse = function(data, callback, errback){
    if (!data.hasOwnProperty('status')){
        return errback("MalformedResponse", "The response from the server did not contain the expected attributes");
    }
    if (!data.hasOwnProperty('data')){
        return errback("MalformedResponse", "The response from the server did not contain the expected attributes");
    }
    if (!data.hasOwnProperty('message')){
        return errback("MalformedResponse", "The response from the server did not contain the expected attributes");
    }
    if (data.status == "FAIL"){
        if (!data.data.hasOwnProperty('exception_class')){
            return errback("MalformedResponse", "The response from the server did not contain the expected attributes");
        }
        if (!data.data.hasOwnProperty('message')){
            return errback("MalformedResponse", "The response from the server did not contain the expected attributes");
        }
        return errback(data['data']['exception_class'], data.data.message);
    }
    return callback(data.data);
};

olwclient.login = function(username, password, callback, errback){
    if (!olwclient.serverUrl){
        jQuery.error( "No serverUrl defined." );
    }

    var login_url = olwclient.serverUrl + "/accounts/ajax_login";
    var data = {
        "password": password,
        "username": username
    };
    $.getJSON(login_url, data, function(data){
        olwclient.handleJSONResponse(data, callback, errback);
    }).fail(function( jqxhr ) {
        olwclient.handleJSONResponse(jqxhr.responseJSON, callback, errback);
    });
};

olwclient.Host = function(data){
    for (var propName in data){
        if (propName == "Jobs"){
            continue;
        }
        if (data.hasOwnProperty(propName))this[propName] = data[propName]
    }
    return this;
};

olwclient.Host.prototype.jobs = function(callback, errback, filters){
    if (!filters)filters={};
    filters['host_name'] = self.host_name;
    olwclient.Job.getJobList(callback, errback, filters);
};

olwclient.Host.getHost = function(hostName, callback, errback){
    return olwclient.getObject("/hosts/" + hostName, olwclient.Host, callback, errback);
};

olwclient.Host.getHostList = function(callback, errback){
    return olwclient.getObjectList("/hosts/", olwclient.Host, callback, errback);
};


olwclient.User = function(data){
    for (var propName in data){
        if (propName == "Jobs"){
            continue;
        }
        if (data.hasOwnProperty(propName))this[propName] = data[propName]
    }
    return this;
};

olwclient.User.prototype.jobs = function(callback, errback, filters){
    if (!filters)filters={};
    filters['host_name'] = self.username;
    olwclient.Job.getJobList(callback, errback, filters);
};

olwclient.User.getUser = function(userName, callback, errback){
    olwclient.getObject("/users/" + userName, olwclient.Queue, callback, errback);
};

olwclient.User.getUserList = function(callback, errback){
    return olwclient.getObjectList("/users/", olwclient.User, callback, errback);
};



olwclient.Queue = function(data){
    for (var propName in data){
        if (propName == "Jobs"){
            continue;
        }
        if (data.hasOwnProperty(propName))this[propName] = data[propName]
    }
    return this;
};

olwclient.Queue.getQueue = function(queueName, callback, errback){
    olwclient.getObject("/queues/" + queueName, olwclient.Queue, callback, errback);
};

olwclient.Queue.getQueueList = function(callback, errback){
    return olwclient.getObjectList("/queues/", olwclient.Queue, callback, errback);
};

olwclient.Queue.prototype.jobs = function(callback, errback, filters){
    if (!filters)filters = {};
    filters['queue_name'] = self.name;
    olwclient.Job.getJobList(callback, errback, filters);
};


olwclient.Job = function(data){
    var jobObject = this;

    olwclient.Host.getHost(data['submission_host'], function(host){
        jobObject.submission_host = host;
    }, function(error, message){
       console.log(error + ": " + message);
    });

    olwclient.Host.getHostList(function(hosts){
        jobObject.execution_hosts = [];
        var i, j;
        for (i = 0; i < hosts.length; i++){
            for (j = 0; j < data['execution_hosts'].length; j++){
                var all_host = hosts[i];
                var sub_host = data['execution_hosts'][j];
                if (all_host['name'] == sub_host['name']){
                    all_host.num_processors = sub_host['num_processors'];
                    jobObject.execution_hosts.push(all_host);
                }
            }
        }
    }, function(error, message){
        console.log(error + ": " + message);
    });

    for (var propName in data){
        if (propName == "submission_host" || propName == "execution_hosts"){
            continue;
        }else if (data.hasOwnProperty(propName))this[propName] = data[propName];
    }
    return this;
};

olwclient.Job.getJob = function(job_id, array_index, callback, errback){
    olwclient.getObject("/job/" + job_id + "/" + array_index, olwclient.Job, callback, errback);
};

olwclient.Job.getJobList = function(callback, errback, filters){
    var url = "/jobs/";
    if (filters){
        url += "?" + $.param(filters);
    }
    return olwclient.getObjectList(url, olwclient.Job, callback, errback);
};


olwclient.Queue.prototype.jobs = function(callback, errback, filters){
    if (!filters)filters={};
    filters['queue_name'] = self.name;
    olwclient.Job.getJobList(callback, errback, filters);
};

olwclient.getObject = function(subUrl, type, callback, errback){
    if (!olwclient.serverUrl)jQuery.error("No serverUrl defined.");
    var url = olwclient.serverUrl + subUrl;

    $.getJSON(url, data, function(data){
        olwclient.handleJSONResponse(data, function(parsed_data){
            callback(new type(parsed_data));
        }, errback);
    }).fail(function( jqxhr ) {
        olwclient.handleJSONResponse(jqxhr.responseJSON, callback, errback);
    });
};

olwclient.getObjectList = function(subUrl, type, callback, errback){
    if (!olwclient.serverUrl)jQuery.error("No serverUrl defined.");

    var url = olwclient.serverUrl + subUrl;

    $.getJSON(url, data, function(data){
        olwclient.handleJSONResponse(data, function(parsed_data){
            var objects = [];
            var i;
            for (i = 0; i < parsed_data.length; i++)objects.push(new type(parsed_data[i]));
            callback(objects);
        }, errback);
    }).fail(function( jqxhr ) {
        olwclient.handleJSONResponse(jqxhr.responseJSON, callback, errback);
    });
};


