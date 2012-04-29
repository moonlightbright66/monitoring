#!/usr/bin/env python
from daemonwatch import *
import json
config = json.loads(file("jabber.passwd").read())
action = XMPP(
	"sebastien@ffctn.com",
	"Daemonwatch: testing iteration #${iteration}@${timestamp}=${result}",
	config["user"], config["password"]
)
Monitor(
	Service(
		name = "test-action-email",
		monitor = (
			Fail(   Time.s(10), actions=action),
			Succeed(Time.s(5),  actions=action)
		)
	)
).run()
