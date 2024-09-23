from faker import Faker


class UniqueDataGenerator:
    def __init__(self):
        self.faker = Faker()
        self.generated_data = {
            "movie_comment": []
        }

    def generate_unique_movie_comment(self):
        comment = self.faker.text()
        while len(comment.split()) < 5 or comment in self.generated_data["movie_comment"]:
            comment = self.faker.text()
        self.generated_data["movie_comment"].append(comment)
        return comment

