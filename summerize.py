import requests



import requests

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
headers = {"Authorization": "Bearer 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"}

filename='audio1.mp3'

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("audio1.mp3")


print(output)



API_URL2 = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
headers2 = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL2, headers=headers2, json=payload)
	return response.json()

story = """Once upon a time, a speedy Rabbit boasted of his lightning-fast legs. He'd zip across meadows, leaving even the wind breathless. One sunny day, he encountered a plodding Turtle, munching on a dandelion with unhurried patience.
"Look at you, waddling like a sack of potatoes!" the Rabbit jeered. "I bet I could race you to that oak tree and back before you reach the first branch!"
The Turtle, unfazed, replied with a slow smile, "Perhaps, speedy friend. But why not find out?"
Thus, the forest creatures gathered to witness the unusual race. The Rabbit, brimming with overconfidence, shot off like a furry bullet. The Turtle, meanwhile, continued his steady crawl, each step deliberate and unhurried.
Reaching a cool patch beneath a willow tree halfway through, the Rabbit, feeling victory in his whiskers, decided to rest. He stretched out and drifted into a nap, lulled by the chirping birds.
But the Turtle, unyielding in his pace, kept inching closer to the finish line. The sun climbed higher, painting the forest with golden light. Finally, the Rabbit woke with a startled snort. Panic gnawed at him as he realized he'd overslept! He raced towards the finish line, his heart pounding like a drum.
But alas, it was too late. The Turtle, though slow and steady, had never faltered. He crossed the finish line first, greeted by the cheering crowd.
The Rabbit, defeated and humbled, learned a valuable lesson that day. Speed wasn't everything, he realized. It was perseverance, unwavering and patient, that truly crossed the finish line. And so, the race that started as a boast became a testament to the power of a steady pace and a determined heart."""



output = query({
	"inputs": story})

print(output)

