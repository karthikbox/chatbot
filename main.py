#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys
import json
import pprint


try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )

    import apiai


# demo agent acess token: e5dc21cab6df451c866bf5efacb40178

CLIENT_ACCESS_TOKEN = '32c83732db0a4ea68afe48d430abc081'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    pp = pprint.PrettyPrinter(indent=4)

    while True:
        print(u"> ", end=u"")
        user_message = raw_input()

        if user_message == u"exit":
            break

        request = ai.text_request()
        request.query = user_message

        response = json.loads(request.getresponse().read())

        result = response['result']
        action = result.get('action')
        actionIncomplete = result.get('actionIncomplete', False)

        print(u"< %s" % response['result']['fulfillment']['speech'])

        if action is not None:
            if action == u"travel_options":
                pp.pprint(result)
                print(result)
                parameters = result['parameters']

                source = parameters.get('source')
                destination = parameters.get('destination')

                print (
                    'source: %s, destination: %s' %
                    (
                        source if source else "null",
                        destination if destination else "null"
                    )
                )

                if not actionIncomplete:
                    print(u"...Sending Message...")
                    break


if __name__ == '__main__':
    main()
