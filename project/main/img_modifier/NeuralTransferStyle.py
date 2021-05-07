import traceback
from os import path

import PIL
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
        stylize_image(content_path,style_path) :
            Applies Neural Style Transfer to Content Image from Style Image and Returns the Stylized Image
        __img_to_numpy_arr(img):
            Converts a PIL Image to a Numpy Array suitable for Tensorflow
        __load(image_path) :
            Loads an image as a numpy array and normalizes it from the given image path
        __resize(img, max_size):
            Resize a Numpy Array from an image according to a max size
        __show_plots():
            Displays content, style and stylized images
    """

    def __init__(self, model_path, content=None):
        """
        Constructs the Fast Arbitrary Image Style Transfer Model from Tensorflow Hub

        Parameters
        ----------
            model_path : str
                Path for the model used by Tensorflow
        """
        assert isinstance(content, PIL.Image.Image)

        self.model = hub.load(model_path)
        self.content = content
        self.style = None
        self.stylized = None

    def stylize_image(self, content_path=None, style_path=None, show_plots=False):
        """
        Applies Neural Style Transfer to Content Image from Style Image and Returns the Stylized Image

        Parameters
        ----------
            content_path : str
                path of the Content Image
            style_path : str
                path of the Style Image
            show_plots : bool
                to show content, style and stylized images

        Returns
        -------
            A PIL Image instance
        """
        try:
            if self.content is None:
                self.content = NeuralTransferStyle.__load(content_path)
            else:
                self.content = NeuralTransferStyle.__img_to_numpy_arr(self.content)
                self.content = NeuralTransferStyle.__resize(self.content, 800)

            img_height = self.content.shape[1]
            img_width = self.content.shape[2]

            self.style = NeuralTransferStyle.__load(style_path, target_size=(img_height, img_width))
            self.stylized = self.model(tf.image.convert_image_dtype(self.content, tf.float32),
                                       tf.image.convert_image_dtype(self.style, tf.float32))[0]
            self.__show_plots() if show_plots else None

            return tf.keras.preprocessing.image.array_to_img(self.stylized[0])
        except Exception as e:
            print("Error Occurred :", e)
            traceback.print_exc()
            return None

    @staticmethod
    def __img_to_numpy_arr(img):
        """
        Converts a PIL Image to a Numpy Array suitable for Tensorflow

        Parameters
        ----------
            img : PIL.Image.Image
                Image to convert

        Returns
        -------
            img : Numpy Array
        """
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = np.array([img / 255.0])
        return img

    @staticmethod
    def __load(image_path, max_size=800, target_size=None):
        """
        Loads an image as a numpy array and normalizes it from the given image path

        Parameters
        ----------
            image_path : str
                File path of the image
            target_size : (int, int)
                Size of the image. Either `None` (default to original size) or tuple of ints `(img_height, img_width)`.

        Returns
        -------
            img : Numpy Array
        """
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=target_size)
        img = NeuralTransferStyle.__img_to_numpy_arr(img)
        img = NeuralTransferStyle.__resize(img, max_size)
        return img

    @staticmethod
    def __resize(img, max_size):
        """
        Resize a Numpy Array from an image according to a max size

        Parameters
        ----------
            img : Numpy Array
                Image tensor to be resized
            max_size : int
                Max height or width

        Returns
        -------
            img : Numpy Array
        """
        img_height = img.shape[1]
        img_width = img.shape[2]

        if max([img_height, img_width]) > max_size:
            if img_height > img_width:
                new_height = max_size
                new_width = new_height * (img_width / img_height)
                new_width = int(new_width)
            else:
                new_width = max_size
                new_height = new_width * (img_height / img_width)
                new_height = int(new_height)
            img = tf.image.resize(img, size=(new_height, new_width))
        return img

    def __show_plots(self):
        """
        Displays content, style and stylized images

        Parameters
        ----------

        Returns
        -------
            None
        """
        plt.imshow(self.content[0])
        plt.title('Content Image')
        plt.axis('off')
        plt.show()

        plt.imshow(self.style[0])
        plt.title('Style Image')
        plt.axis('off')
        plt.show()

        plt.imshow(self.stylized[0])
        plt.title('Stylized Image')
        plt.axis('off')
        plt.show()
