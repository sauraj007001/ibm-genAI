import requests

# Replace this with your actual Hugging Face API token
API_TOKEN = "your_huggingface_api_token"
API_URL = "https://api-inference.huggingface.co/models/your-model-name"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def generate_resume(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 500}
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"]
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    print("Welcome to the AI Resume Generator!")
    name = input("Enter your full name: ")
    role = input("Enter your desired role: ")
    experience = input("Summarize your experience: ")
    skills = input("List your skills (comma-separated): ")

    prompt = (
        f"Generate a professional resume for the following information:\n"
        f"Name: {name}\n"
        f"Role: {role}\n"
        f"Experience: {experience}\n"
        f"Skills: {skills}\n\n"
        f"Resume:"
    )

    resume_output = generate_resume(prompt)
    print("\nGenerated Resume:\n")
    print(resume_output)
