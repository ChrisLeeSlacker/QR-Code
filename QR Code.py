import pyqrcode

# TODO: Check if works with input
def generate_qr():
    # Link input:
    link_to_post = input('What is the adress?:\n')
    # Static link for test
    # link_to_post = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    url = pyqrcode.create(link_to_post)
    url.svg('url.png', scale=8)
    print("Printing QR code")
    print(url.terminal())


if __name__ == '__main__':
    generate_qr()
