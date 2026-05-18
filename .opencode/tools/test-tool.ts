import { tool } from "@opencode-ai/plugin"

export default tool({
  description: "Generation of a phrase from the words of the NATO/ICAO phonetic alphabet",
  args: {
    phraseLen: tool.schema.number().describe("Count of word to generate phrase"),
  },
  async execute(args) {
    const icaoWords = [
    'Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo',
    'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliett',
    'Kilo', 'Lima', 'Mike', 'November', 'Oscar',
    'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
    'Uniform', 'Victor', 'Whiskey', 'X‑ray', 'Yankee', 'Zulu'
    ];

    const icaoWordsCount = icaoWords.length;
    const maxWordsCount = Math.min(args.phraseLen, icaoWordsCount);
    let result = '';

    for (let i = 0; i < maxWordsCount; i++) {
        const randIndex = Math.floor(Math.random() * icaoWordsCount);
        if (icaoWords[randIndex]) {
            result = `${result} ${icaoWords[randIndex]}`;
        }
    }

    return `Generated phrase with ${args.phraseLen} words: ${result}`
  },
})