import pyqrcode

class qr_codes:
    def generate_code(self, url):
        return pyqrcode.create(url)

    def render_qr_code(self, url, scale, type):
        render_qr_image = self.generate_code(url=url)
        if type == "png":
            render_qr_image.png('qrcode.png', scale=scale)
        elif type == "svg":
            render_qr_image.svg('qrcode.svg', scale=scale)

