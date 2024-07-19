from django.conf import settings
from openai import OpenAI

client = OpenAI(
  api_key=settings.OPENAI_API_KEY,
  organization='org-39YJrGRD0ZiVFBLBY2Y1S4XR',
  project='proj_BCHuy5hJwSRE1SDSXPmOcU2T',
)

def get_skill_suggestions(branch, job_title, experience, satisfaction):
    prompt = (
        f"Based on the following details, suggest at least 10 relevant skills:\n"
        f"Branch: {branch}\n"
        f"Job Title: {job_title}\n"
        f"Experience: {experience}\n"
        f"Satisfaction: {satisfaction}\n"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )

    suggestions = response.choices[0].message.content.strip().split('\n')
    return suggestions
