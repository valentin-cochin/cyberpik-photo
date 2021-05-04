from os import path

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub


class NeuralTransferStyle:
    """
    A class to apply and run style transfer for a Content Image from a given Style Image
    Attributes
    ----------
        model : Hub Module
        content : Numpy Array
        style : Numpy Array
        stylized : Tensorflow Eager Tensor

    Methods
    -------
        load(image_path) :
            Loads an image as a numpy array and normalizes it from the given image path
        stylize_image(content_path,style_path) :
            Applies Neural Style Transfer to Content Image from Style Image and Displays the Stylized Image
    """

    def __init__(self):
        """
        Constructs the Fast Arbitrary Image Style Transfer Model from Tensorflow Hub

        Parameters
        ----------
            None
        """
        # Fast arbitrary image style transfer model from Tensorflow Hub
        base_path = path.dirname(__file__)
        filepath = path.abspath(
            path.join(base_path, '..', '..', '..', 'ml_models', 'magenta_arbitrary-image-stylization-v1-256_2'))

        self.model = hub.load(filepath)
        self.content = None
        self.style = None
        self.stylized = None

    # @staticmethod
    def load(self, image_path):
        """
        Loads an image as a numpy array and normalizes it from the given image path

        Parameters
        ----------
            image_path : str
                File path of the image

        Returns
        -------
            img : Numpy Array
        """
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(960, 720))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = np.array([img / 255.0])
        return img

    def stylize_image(self, content_path, style_path):
        """
        Applies Neural Style Transfer to Content Image from Style Image and Displays the Stylized Image

        Parameters
        ----------
            content_path : str
                path of the Content Image
            style_path : str
                path of the Style Image

        Returns
        -------
            None
        """
        try:
            self.content = self.load(content_path)
            self.style = self.load(style_path)
            self.stylized = self.model(tf.image.convert_image_dtype(self.content, tf.float32),
                                       tf.image.convert_image_dtype(self.style, tf.float32))[0]
            plt.imshow(self.content[0])
            plt.title('Content Image')
            plt.show()
            plt.imshow(self.style[0])
            plt.title('Style Image')
            plt.show()
            plt.imshow(self.stylized[0])
            plt.title('Stylized Image')
            plt.show()
        except Exception as e:
            print("Error Occurred :", e)


if __name__ == "__main__":
    nst = NeuralTransferStyle()
