class Article:
    """
    A class to represent an article with a title, author, and content.
    """

    def __init__(self, title: str, author: str, content: str):
        """
        Initialize an Article instance.

        :param title: The title of the article
        :param author: The author of the article
        :param content: The content of the article
        """
        self.title = title
        self.author = author
        self.content = content

    def summary(self, word_limit: int = 50) -> str:
        """
        Generate a summary of the article content.

        :param word_limit: The maximum number of words in the summary
        :return: A string containing the summary
        """
        words = self.content.split()
        if len(words) <= word_limit:
            return self.content
        return ' '.join(words[:word_limit]) + '...'

    def __str__(self) -> str:
        """
        Return a string representation of the article.

        :return: A string containing the title and author
        """
        return f"'{self.title}' by {self.author}"