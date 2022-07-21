init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_playtime",
            category=["us"],
            prompt="playtime",
            pool=True,
            unlocked=True
        )
    )

label otter_playtime:
    m "[current_total_playtime]."
return
