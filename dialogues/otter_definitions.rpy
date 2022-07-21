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
    m "We've been together for [mas_getTotalPlaytime()]."
    m "I love you, [player]!"
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
    m "Today, we spent [mas_getSessionLength()] together."
    m "I love you, [player]!"
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
    m "I waited for you for [mas_getAbsenceLength()]."
    m "I missed you, [player]!"
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
    m "You got here on [mas_getCurrSeshStart()]."
    m "I love you, [player]!"
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
    m "You visited me for the last time on [mas_getLastSeshEnd()]."
    m "I love you, [player]!"
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
    m "You visited me [mas_getTotalSessions()] times."
    m "I love you, [player]!"
return "love"
