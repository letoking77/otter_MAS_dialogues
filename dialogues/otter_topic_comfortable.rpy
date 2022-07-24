init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_topic_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_topic_comfortable",
            category=["monika"],
            prompt="Don't your elbows hurt to be in that position for so long?",
            pool=True,
            unlocked=True
        )
    )

label otter_topic_comfortable:
    m "Oh! "
    extend "Now that's an interesting question."
    m "Thank you for worrying about my comfort, [player]."
    m "Well, as you might have already noticed, I change my position every now and then."
    m "Because yes! It hurts sometimes!"
    m "One day I looked over at my arms before bed and they were kind of red."
    m "But don't worry! I'm okay!"
    m "After all, some amazing people even went out of their way to make me some elbow cushions!"
    m "So that my arms don't hurt from the contact with the hard table."
    m "Isn't that nice?"
    m "I have to thank my lovely [player] for being so kind and thoughtful."
    m "I love you!"
    
return "love"
