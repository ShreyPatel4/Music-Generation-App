
import magenta.music as mm
from magenta.models.music_vae import TrainedModel
import tensorflow.compat.v1 as tf
import os

tf.disable_v2_behavior()

class MelodyGenerator:
    def __init__(self):
        checkpoint_path = 'models/cat-mel_2bar_big.ckpt'
        if not os.path.exists(checkpoint_path + '.index'):
            os.makedirs('models', exist_ok=True)
            tf.keras.utils.get_file(
                'cat-mel_2bar_big.tar',
                origin='http://download.magenta.tensorflow.org/models/music_vae/cat-mel_2bar_big.tar',
                cache_dir='models',
                cache_subdir=''
            )
            import tarfile
            tar = tarfile.open('models/cat-mel_2bar_big.tar')
            tar.extractall(path='models')
            tar.close()

        self.model = TrainedModel(
            config=mm.music_vae.configs.CONFIG_MAP['cat-mel_2bar_big'],
            batch_size=4,
            checkpoint_dir_or_path=checkpoint_path
        )

    def generate(self, primer_sequence: mm.NoteSequence, temperature: float, total_bars: int) -> mm.NoteSequence:
        z = self.model.sample(n=1, length=total_bars * 32, temperature=temperature)
        generated_sequence = self.model.decode(z, length=total_bars * 32)
        return generated_sequence[0]
