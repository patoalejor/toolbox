import tensorflow as tf 

def limit_gpu_memory(logger, memory:int=32768):
    # Set up GPU usage to specific memory
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        # Restrict TensorFlow to only allocate 1GB of memory on the first GPU
        try:
            tf.config.set_logical_device_configuration(gpus[0],[tf.config.LogicalDeviceConfiguration(memory_limit=memory)])
            logical_gpus = tf.config.list_logical_devices('GPU')
            logger.debug(f"GPUS: {len(gpus)} Physical GPUs {len(logical_gpus)} Logical GPUs")
        except RuntimeError as e:
            # Virtual devices must be set before GPUs have been initialized
            logger.warning(e)


