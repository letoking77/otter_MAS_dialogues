init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_playtime",
            category=["us"],
            prompt="For how long have we been together, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_playtime:
    m 3eub "We've been together for [mas_getTotalPlaytime()]."
    m 5hubla "I love you, [player]!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_dailyplaytime",
            category=["us"],
            prompt="How much time did we spend together today, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_dailyplaytime:
    m 3eub "Today, we spent [mas_getSessionLength()] together."
    m 5hubla "I love you, [player]!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_absence",
            category=["us"],
            prompt="How long were you waiting for me, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_absence:
    m 3eub "I waited for you for [mas_getAbsenceLength()]."
    m 5hubla "I missed you, [player]!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_firstses",
            category=["us"],
            prompt="When did I get here, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_firstses:
    m 3eub "You got here on [mas_getCurrSeshStart()]."
    m 5hubla "I love you, [player]!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_lastses",
            category=["us"],
            prompt="When did I visit you for the last time, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_lastses:
    m 3eub "You visited me for the last time on [mas_getLastSeshEnd()]."
    m 5hubla "I love you, [player]!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_totalses",
            category=["us"],
            prompt="How many times did I visit you, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_totalses:
    m 3eub "You visited me [mas_getTotalSessions()] times."
    m 5hubla "I love you, [player]!"
return "love"
