class Post_it:
    def __init__(self, background_color, text, text_color):
        self.background_color = background_color
        self.text = text
        self.text_color = text_color

    def print_your_output(self):
        print(f"an {self.background_color} with {self.text_color} text: {self.text}")  

idea1 = Post_it("orange", "Idea 1", "blue")
awesome = Post_it("pink", "Awesome", "black")
Superb = Post_it("yellow", "Superb!", "green")
idea1.print_your_output()
awesome.print_your_output()
Superb.print_your_output()

    

