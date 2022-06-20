from emora_stdm import DialogueFlow, NatexNLU

chatbot = DialogueFlow('start', end_state='end')
transitions = {
    'state': 'start',
    '"Welcome to Madam Emora\'s Shop of Mysteries! Can I take your fortune?"': {
        '[{yes, sure, I guess, why not, okay}]': {
            '"Excellent! Let me see your palm child. Ready?"': {
                'state': 'taking-fortune',
                '#UNX': {
                    '`Oh dear. This is unfortunate. I see dark things in your future... I can help you uncover them. '
                    'But at a cost... (59.99: our dark things uncoverer plan) Will you be paying cash or credit?`': {
                        'state': 'payment-choice',
                        '[{cash, credit}]': {
                            "`Excellent! I foresee that... you will slip in a puddle tommorow! Aren't you glad you "
                            "found that out? Thanks for your patronage. Come again!`": 'user-resp',
                            "`Excellent! I foresee that... you will lose your glasses tommorow! Aren't you glad you "
                            "found that out? Thanks for your patronage. Come again!`": 'user-resp',
                            "`Excellent! I foresee that... you will stain your shirt tommorow! Aren't you glad you "
                            "found that out? Thanks for your patronage. Come again!`": {
                                'state': "user-resp",
                                "[{bad, poor, ripoff}]": {
                                    '"Well there aren\'t any refunds"': 'end'
                                },
                                'error': 'end'
                            }
                        },
                        '[{check}]': {
                            '"This is am old fashioned shop, but not that old fashioned. '
                            'Cash or credit?"': 'payment-choice'
                        },
                        '#GATE': {
                            'score': 0.75,
                            '"Are you really willing to take risks with your fate? '
                            'I ask again: Cash or credit?"': 'payment-choice'
                        },
                        'error': {
                            'score': 0.5,
                            '"I really suggest you pick an option."': 'payment-choice'
                        }
                    }
                }
            },
        },
        'error': {
            '"Come now! What are you afraid of? Give me your palm. Ready?"': 'taking-fortune'
        }
    }
}
chatbot.load_transitions(transitions)

if __name__ == "__main__":
    chatbot.run(debugging=False)
