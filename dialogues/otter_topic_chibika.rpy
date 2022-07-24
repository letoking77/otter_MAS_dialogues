init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_topic_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_topic_chibika",
            prompt="Chibika plushie",
            category=["you"],
            random=True
        )
    )

label otter_topic_chibika:
    m "[player], I've been thinking."
    m "I know every game has its merch, and fans love to buy it..."
    m "And of course, this game also has its plushies, physical editions and such."
    m "Which led me to be curious about something..."
    m "Do you own any 'DDLC' merch?"
$ _history_list.pop()
menu:
    "No":
    "Oh! That's fair."
    "Merch is not cheap, after all."
    #blahblah chibika
    "Yes":
    #blahblah but do you have chjibika
        $ _history_list.pop()
        menu:
        m "Do you have one?"
        "Yes":
        #blahblah chibika hold her at night and think of me
        "No":
        #blahblah chibika
