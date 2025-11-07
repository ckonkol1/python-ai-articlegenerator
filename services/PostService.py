import os
from openai import OpenAI

class PostService:

    def create_post(self, post):
        if post.model == "gpt5":
            return self.call_openapi(post)
        else:
            raise ValueError(f"Model {post.model} is not supported.")
        
    def call_openapi(self, post):
        API_KEY = os.getenv("OPENAI_API_KEY")

        if API_KEY is None:
            raise Exception("API key is missing")
        
        client = OpenAI()

        completion = client.chat.completions.create(
            model="gpt-4o-mini-search-preview",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional research assistant."
                        f"Find articles that summarize {post.topic}. These articles should be from professional sources like Microsoft, ACM, or any other reputable site. "
                        "Do not include conversational text, suggestions, or follow-up offers."
                    )
                }
            ],
        )

        news_articles = completion.choices[0].message.content
                
        
        system_message = """
        You are a helpful assistant who's job is to accurately summarize long series of 
        articles provided to you by the user and write up a compelling and easy to 
        digest social media post.
        """

        prompt = f"""
        The following is a series of articles {post.topic}. Please summarize
        the articles and write a compelling blog post highlighting the key points about each article.

        The post should be short and concise and should not be more than 500 words. 
        It should also include a reference section at the end with links to each article.
        Do not include conversational text, suggestions, or follow-up offers.
        
        {news_articles}
        """

        completion = client.chat.completions.create(
            model=post.model,
            messages=[
                {"role": "system", "content": system_message},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content  