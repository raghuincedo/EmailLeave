requests_template = {
   "id":"12weeqe2344",
   "state":"AWATING SUPERVISOR RESPONSE",
   "status":"COMPLETED",
   "leaveDateList":[
      "23/12/2018",
      "23/12/2018"
   ],
   "requestorEmail":"abhik@gmail.com",
   "approverEmail":"dev@gmail.com",
   "requestReason":"FAMILY PROBLEM",
   "mailList":[
      {
         "mailReceivedDateTime":"23/12/2018",
         "mailSender":" abhik@gmail.com ",
         "mailType":" NEW REQUEST ",
         "mailCCList":[

         ],
         "content":" I would like a leave from --------- ",
         "subject":"sub:leave request "
      },
      {
         "mailReceivedDateTime":"23/12/2018",
         "mailSender":"System",
         "mailType":" REQUEST RECEIVED CONFIRMATION "
      }
   ]
}

users_template = {
   "emailId":" abhik@gmail.com",
   "name":"Abhik Patel",
   "location":"United States",
   "currentSupervisorEmail":"dev@gmail.com",
   "currentSupervisorName":"DevangPatel",
   "previousSupervisors":[
      {
         "email":"ashutosh@gmail.com",
         "name":"Ashutosh",
         "from":"23/12/2016",
         "to":"23/12/2017"
      }
   ]
}

raw_emails_template = {
   "receivedFrom":"abhik@gmail.com",
   "mailReceivedDateTime":"23/12/2018",
   "rawContent":"Raw Email in String or Json format",
   "requestId":"RN6025511402180350"
}

leave_dates_template = {
   "location" : "UNITED STATES",
   "leaveDateListForCurrentYear" : "23/12/2018"
}