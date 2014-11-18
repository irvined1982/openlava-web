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

olwclient._serverUrl = null;

olwclient.serverUrl = function(url) {
    if (url !== undefined) {
        if (url.slice(-1) == "/") {
            url = url.substring(0, url.length - 1);
        }
        olwclient._serverUrl = url;
    }
    return olwclient._serverUrl;
};

olwclient.handleJSONResponse = function(data, callback, errback){
    if (!data){
        return errback("Invalid response from server");
    }
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
    if (!olwclient._serverUrl){
        jQuery.error( "No serverUrl defined." );
    }

    var login_url = olwclient._serverUrl + "/accounts/ajax_login";
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

olwclient.Host.prototype.close = function(callback, errback){
    olwclient.closeHost(this.name, callback, errback);
};

olwclient.closeHost = function(hostName, callback, errback){
    var url = "/hosts/" + hostName + "/close";
    olwclient.executeCommand(url, callback, errback)
};

olwclient.Host.prototype.open = function(callback, errback){
    olwclient.openHost(this.name, callback, errback);
};

olwclient.openHost = function(hostName, callback, errback){
    var url = "/hosts/" + hostName + "/open";
    olwclient.executeCommand(url, callback, errback)
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

olwclient.Queue.prototype.close = function(callback, errback){
    return olwclient.closeQueue(this.name, callback, errback);
};

olwclient.closeQueue = function(queueName, callback, errback){
    var url = "/queues/" + queueName + "/close";
    olwclient.executeCommand(url, callback, errback)
};

olwclient.Queue.prototype.open = function(callback, errback){
    return olwclient.openQueue(this.name, callback, errback);
};

olwclient.openQueue = function(queueName, callback, errback){
    var url = "/queues/" + queueName + "/open";
    olwclient.executeCommand(url, callback, errback)
};


olwclient.Queue.prototype.activate = function(callback, errback){
    return olwclient.activateQueue(this.name, callback, errback);
};

olwclient.activateQueue = function(queueName, callback, errback){
    var url = "/queues/" + queueName + "/activate";
    olwclient.executeCommand(url, callback, errback);
};

olwclient.Queue.prototype.inactivate = function(callback, errback){
    return olwclient.inactivateQueue(this.name, callback, errback);
};

olwclient.inactivateQueue = function(queueName, callback, errback){
    var url = "/queues/" + queueName + "/inactivate";
    olwclient.executeCommand(url, callback, errback)
};


olwclient.Job = function(data){

    for (var propName in data){
        if (data.hasOwnProperty(propName))this[propName] = data[propName];
    }
    return this;


/*
    var jobObject = this;
    olwclient.Host.getHost(data['submission_host']['name'], function(host){
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
    });*/

};


olwclient.Job.prototype.submit_time_datetime = function(){
    var submit_time_datetime = new Date(0);
    submit_time_datetime.setUTCSeconds(this.submit_time);
    return submit_time_datetime;
};

olwclient.Job.prototype.end_time_datetime = function(){
    if (this.end_time < 1){
        return null;
    }
    var end_time_datetime = new Date(0);
    end_time_datetime.setUTCSeconds(this.end_time);
    return end_time_datetime;
};

olwclient.Job.prototype.start_time_datetime = function(){
    if (this.start_time < 1){
        return null;
    }
    var start_time_datetime = new Date(0);
    start_time_datetime.setUTCSeconds(this.start_time);
    return start_time_datetime;
};

olwclient.Job.prototype.predicted_start_time_datetime = function(){
    if (this.predicted_start_time_datetime < 1){
        return null;
    }
    var predicted_start_time_datetime = new Date(0);
    predicted_start_time_datetime.setUTCSeconds(this.predicted_start_time);
    return predicted_start_time_datetime;
};

olwclient.Job.prototype.reservation_time_datetime = function(){
    if (this.reservation_time_datetime < 1){
        return null;
    }
    var reservation_time_datetime = new Date(0);
    reservation_time_datetime.setUTCSeconds(this.reservation_time);
    return reservation_time_datetime;
};

olwclient.Job.dateToString = function(date){
    return date.toDateString() + " " + date.toLocaleTimeString();
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

olwclient.Job.prototype.kill = function(callback, errback){
    olwclient.killJob(this.job_id, this.array_index, callback, errback);
};

olwclient.killJob = function(job_id, array_index, callback, errback){
    olwclient.executeCommand("/job/" + job_id + "/" + array_index + "/kill", callback, errback)
};

olwclient.Job.prototype.requeue = function(hold, callback, errback){
    olwclient.requeueJob(this.job_id, this.array_index, hold, callback, errback);
};

olwclient.requeueJob = function(job_id, array_index, hold, callback, errback){
    var url = "/job/" + job_id + "/" + array_index + "/requeue";
    if (hold)url += "?hold=True";
    console.log(url);
    olwclient.executeCommand(url, callback, errback)
};

olwclient.Job.prototype.suspend = function(callback, errback){
    olwclient.suspendJob(this.job_id, this.array_index, callback, errback);
};

olwclient.suspendJob = function(job_id, array_index, callback, errback){
    var url = "/job/" + job_id + "/" + array_index + "/suspend";
    olwclient.executeCommand(url, callback, errback)
};

olwclient.Job.prototype.resume = function(callback, errback){
    olwclient.resumeJob(this.job_id, this.array_index, callback, errback);
};

olwclient.resumeJob = function(job_id, array_index, callback, errback){
    var url = "/job/" + job_id + "/" + array_index + "/resume";
    olwclient.executeCommand(url, callback, errback)
};



olwclient.executeCommand = function(subUrl, callback, errback){
    var fullUrl = olwclient._serverUrl + subUrl;
    console.log(fullUrl);
    $.getJSON(fullUrl, null, function(data){
        olwclient.handleJSONResponse(data, function(parsed_data){
            callback(parsed_data);
        }, errback);
    }).fail(function( jqxhr ) {
        olwclient.handleJSONResponse(jqxhr.responseJSON, callback, errback);
    });
};

olwclient.getObject = function(subUrl, type, callback, errback){
    if (!olwclient._serverUrl)jQuery.error("No serverUrl defined.");
    var url = olwclient._serverUrl + subUrl;

    $.getJSON(url, null, function(data){
        olwclient.handleJSONResponse(data, function(parsed_data){
            callback(new type(parsed_data));
        }, errback);
    }).fail(function( jqxhr ) {
        olwclient.handleJSONResponse(jqxhr.responseJSON, callback, errback);
    });
};

olwclient.getObjectList = function(subUrl, type, callback, errback){
    if (!olwclient._serverUrl)jQuery.error("No serverUrl defined.");

    var url = olwclient._serverUrl + subUrl;

    $.getJSON(url, null, function(data){
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

olwclient.getHostOverview = function(callback, errback){
    var url =  olwclient._serverUrl + "/overview/hosts";
    $.getJSON(url, null, function(data){
        olwclient.handleJSONResponse(data, callback, errback);
    }).fail(function( jqxhr ) {
        olwclient.handleJSONResponse(jqxhr.responseJSON, callback, errback);
    });
};

olwclient.getJobOverview = function(callback, errback){
    var url =  olwclient._serverUrl + "/overview/jobs";
    $.getJSON(url, null, function(data){
        olwclient.handleJSONResponse(data, callback, errback);
    }).fail(function( jqxhr ) {
        olwclient.handleJSONResponse(jqxhr.responseJSON, callback, errback);
    });
};

olwclient.getSlotsOverview = function(callback, errback){
    var url =  olwclient._serverUrl + "/overview/slots";
    $.getJSON(url, null, function(data){
        olwclient.handleJSONResponse(data, callback, errback);
    }).fail(function( jqxhr ) {
        olwclient.handleJSONResponse(jqxhr.responseJSON, callback, errback);
    });
};

