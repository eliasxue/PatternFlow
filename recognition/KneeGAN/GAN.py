

### Define Model:

## Generator:

def generator(input_dim, num_blocks, latent_dim):
    
    input_layer = tf.keras.Input(latent_dim)

    net = tf.keras.layers.Dense(1024)(input_layer)
    net = tf.keras.layers.Dense(input_dim*input_dim*64)(input_layer)
    net = tf.keras.layers.Reshape((input_dim,input_dim,64))(net)
    net = tf.keras.layers.ReLU()(net)

    net = tf.keras.layers.Conv2DTranspose(64, (3,3), strides=(2,2), padding='same')(net)
    net = tf.keras.layers.Conv2D(64, (3,3), strides=(1,1), padding='same')(net)
    net = tf.keras.layers.ReLU()(net)

    net = tf.keras.layers.Conv2DTranspose(32, (3,3), strides=(2,2), padding='same')(net)
    net = tf.keras.layers.Conv2D(32, (3,3), strides=(1,1), padding='same')(net)
    net = tf.keras.layers.ReLU()(net)

    net = tf.keras.layers.Conv2DTranspose(16, (3,3), strides=(2,2), padding='same')(net)
    net = tf.keras.layers.Conv2D(16, (3,3), strides=(1,1), padding='same')(net)
    net = tf.keras.layers.ReLU()(net)

    net = tf.keras.layers.Conv2D(3, (3,3), strides=(1,1), padding='same')(net)

    model = tf.keras.Model(inputs=input_layer, outputs=net)

    return model


def discriminator(input_dim, num_blocks):

    input_layer = tf.keras.Input(input_dim)
    net = input_layer

    net = tf.keras.layers.Conv2D(16, (3,3), padding='same')(net)
    net = tf.keras.layers.LeakyReLU(alpha=0.2)(net)
    net = tf.keras.layers.MaxPooling2D((2,2), strides=(2,2))(net)

    net = tf.keras.layers.Conv2D(32, (3,3), padding='same')(net)
    net = tf.keras.layers.LeakyReLU(alpha=0.2)(net)
    net = tf.keras.layers.MaxPooling2D((2,2), strides=(2,2))(net)

    net = tf.keras.layers.Conv2D(64, (3,3), padding='same')(net)
    net = tf.keras.layers.LeakyReLU(alpha=0.2)(net)
    net = tf.keras.layers.MaxPooling2D((2,2), strides=(2,2))(net)
    
    net = tf.keras.layers.Flatten()(net)

    net = tf.keras.layers.Dense(256)(net)
    net = tf.keras.layers.LeakyReLU(alpha=0.2)(net)

    net = tf.keras.layers.Dense(1)(net)

    model = tf.keras.Model(inputs=input_layer, outputs=net)

    return model

    