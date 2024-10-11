
import magenta.music as mm
from magenta.models.groovae import groove_model
from magenta.models.shared import sequence_generator_bundle
from magenta.protobuf import generator_pb2, music_pb2
import tensorflow.compat.v1 as tf
import os

tf.disable_v2_behavior()

class GrooveGenerator:
    def __init__(self):
        bundle_path = 'models/groovae_2bar_humanize.bundle'
        if not os.path.exists(bundle_path):
            os.makedirs('models', exist_ok=True)
            tf.keras.utils.get_file(
                'groovae_2bar_humanize.bundle',
                origin='http://download.magenta.tensorflow.org/models/groovae_2bar_humanize.bundle',
                cache_dir='models',
                cache_subdir=''
            )

        self.bundle = sequence_generator_bundle.read_bundle_file(bundle_path)
        generator_map = groove_model.get_generator_map()
        self.generator = generator_map['groovae_2bar_humanize'](checkpoint=None, bundle=self.bundle)
        self.generator.initialize()

    def generate(self, primer_sequence: music_pb2.NoteSequence, temperature: float, total_bars: int) -> music_pb2.NoteSequence:
        total_seconds = total_bars * 4 * 60 / primer_sequence.tempos[0].qpm

        generator_options = generator_pb2.GeneratorOptions()
        generator_options.generate_sections.add(
            start_time=primer_sequence.total_time,
            end_time=primer_sequence.total_time + total_seconds
        )
        generator_options.args['temperature'].float_value = temperature

        sequence = self.generator.generate(primer_sequence, generator_options)
        return sequence
