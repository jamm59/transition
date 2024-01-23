
import pydub, os
def createAudioLabel(path, filename):
    splitTime = 10 * 1000 #in milliseconds
    try:
        sound = pydub.AudioSegment.from_wav(path)
    except pydub.exceptions.CouldntDecodeError:
        return None

    chunks = pydub.utils.make_chunks(sound, splitTime)
    #mid = len(chunks) // 2
    label = chunks[1]
    firstPart = chunks[0]
    secondPart = sum(chunks[2:])

    firstPart.export(f"x1/{filename}_x1.wav", format="wav")
    secondPart.export(f"x2/{filename}_x2.wav", format="wav")
    label.export(f"labels/{filename}_label.wav", format="wav")


def processGenrePath(path):
    for filename in os.listdir(path):
        createAudioLabel(f"{path}/{filename}", "".join(filename.split(".")[:2]))



if __name__ == "__main__":
    for genre in os.listdir("Data/genres_original"):
        processGenrePath(f"Data/genres_original/{genre}")   
    ##createAudioLabel("Data/genres_original/hiphop/hiphop.00067.wav")