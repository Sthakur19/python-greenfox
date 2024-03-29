class BlogPost:
    def __init__(self, authorName, title, text, publicationDate):
        self.authorName = authorName
        self.title = title
        self.text = text
        self.publicationDate = publicationDate
    
    def print_my_blog_post(self):
        print(f" {self.title} titled by {self.authorName} posted at {self.publicationDate} \n {self.text}")
        print(f" ----- ")


blogPost_1 = BlogPost("John Doe", "Lorem Ipsum", "Lorem ipsum dolor sit amet.", "2000.05.04.")
blogPost_2 = BlogPost("Tim Urban", "Wait but why", "A popular long-form, stick-figure-illustrated blog about almost everything.", "2010.10.10.")
blogPost_3 = BlogPost("William Turton", "One Engineer Is Trying to Get IBM to Reckon With Trump", 
"Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.", 
"2017.03.28.")

blogPost_1.print_my_blog_post()
blogPost_2.print_my_blog_post()
blogPost_3.print_my_blog_post()