import requests
import re

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate_response(user_input):
    context = "In the bustling heart of Silicon Valley, nestled amidst the towering edifices of innovation and ambition, stands a company that has become synonymous with technological prowess and market dynamism. Founded in the early 2000s by a trio of visionary entrepreneurs — Sarah Chang, David Nguyen, and Michael Patel — the company emerged as a disruptive force in the realm of e-commerce and digital services.With a relentless focus on user experience and cutting-edge technology, the company swiftly ascended the ranks, carving out a niche for itself in the competitive landscape. Its flagship product, an AI-driven marketplace that seamlessly connects buyers and sellers across the globe, revolutionized the way people engage in online transactions.Driven by a commitment to excellence and a spirit of innovation, the company soon diversified its portfolio, expanding into areas such as cloud computing, artificial intelligence, and digital entertainment. This strategic evolution not only cemented its position as a market leader but also propelled it to new heights of success and influence.As the company's reputation soared, so did its stock price, captivating investors and analysts alike with its remarkable growth trajectory. Fuelled by a potent combination of visionary leadership, strategic foresight, and technological innovation, the company's stock became a symbol of confidence and optimism in the ever-evolving landscape of the global economy.Today, headquartered in the vibrant city of Palo Alto, California, the company continues to push the boundaries of possibility, guided by the pioneering spirit of its founders and fueled by the collective passion and ingenuity of its diverse workforce. With its sights set firmly on the future, the company remains a beacon of inspiration and a testament to the transformative power of innovation in the digital age."

    output = query({
        "inputs": {
            "question": user_input,
            "context": context
        },
    })
    print(output)
    return output['answer']


while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chatbot exits.")
        break
    user_input = re.sub(r"[^a-zA-Z0-9\s]", " ", user_input.lower())
    response = generate_response(user_input)
    
    print("Bot:", response)
