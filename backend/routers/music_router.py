
from fastapi import APIRouter, HTTPException, File, UploadFile
from pydantic import BaseModel
from models.groove_generator import GrooveGenerator
from models.melody_generator import MelodyGenerator
from utils.midi_utils import sequence_to_midi_file
from utils.audio_utils import midi_to_wav
import uuid
import os

router = APIRouter(prefix="/music", tags=["Music Generation"])

groove_gen = GrooveGenerator()
melody_gen = MelodyGenerator()

class DrumRequest(BaseModel):
    tempo: int
    temperature: float
    total_bars: int
    prompt: str

@router.post("/generate_drum_loop")
async def generate_drum_loop(request: DrumRequest):
    try:
        primer_sequence = mm.NoteSequence()
        primer_sequence.tempos.add(qpm=request.tempo)

        sequence = groove_gen.generate(primer_sequence, request.temperature, request.total_bars)

        unique_id = str(uuid.uuid4())
        midi_file = f'output/{unique_id}_drum.mid'
        wav_file = f'output/{unique_id}_drum.wav'
        os.makedirs('output', exist_ok=True)
        sequence_to_midi_file(sequence, midi_file)
        midi_to_wav(midi_file, wav_file)

        return {"audio_file": wav_file}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class MelodyRequest(BaseModel):
    tempo: int
    temperature: float
    total_bars: int
    prompt: str

@router.post("/generate_melody")
async def generate_melody(request: MelodyRequest):
    try:
        primer_sequence = mm.NoteSequence()
        primer_sequence.tempos.add(qpm=request.tempo)

        sequence = melody_gen.generate(primer_sequence, request.temperature, request.total_bars)

        unique_id = str(uuid.uuid4())
        midi_file = f'output/{unique_id}_melody.mid'
        wav_file = f'output/{unique_id}_melody.wav'
        os.makedirs('output', exist_ok=True)
        sequence_to_midi_file(sequence, midi_file)
        midi_to_wav(midi_file, wav_file)

        return {"audio_file": wav_file}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
