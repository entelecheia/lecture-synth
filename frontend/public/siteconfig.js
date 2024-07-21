// Site configuration
export const site = {
  // Preset avatars
  avatars: {
    Man: {
      url: "./assets/avatars/man.glb",
      body: "M",
      avatarMood: "neutral",
      fi: "Mies",
    },
  },

  // Google voices
  googleVoices: {
    "fi-F": { id: "fi-FI-Standard-A" },
    "lv-M": { id: "lv-LV-Standard-A" },
    "lt-M": { id: "lt-LT-Standard-A" },
    "en-F": { id: "en-GB-Standard-A" },
    "en-M": { id: "en-GB-Standard-D" },
  },

  // ElevenLab voices
  elevenVoices: {
    Bella: { id: "EXAVITQu4vr4xnSDxMaL" },
    Elli: { id: "MF3mGyEYCl7XYWbV9V6O" },
    Rachel: { id: "21m00Tcm4TlvDq8ikWAM" },
    Adam: { id: "pNInz6obpgDQGcFmaJgB" },
    Antoni: { id: "ErXwobaYiN019PkySvjV" },
    Arnold: { id: "VR6AewLTigWG4xSOukaG" },
    Domi: { id: "AZnzlk1XvdvUeBnXmlld" },
    Josh: { id: "TxGEqnHWrfWFTfGW9XjX" },
    Sam: { id: "yoZ06aMxZJJ28mfd3POQ" },
  },

  // Microsoft voices
  microsoftVoices: {
    "fi-Selma": { lang: "fi-FI", id: "fi-FI-SelmaNeural" },
    "fi-Noora": { lang: "fi-FI", id: "fi-FI-NooraNeural" },
    "fi-Harri": { lang: "fi-FI", id: "fi-FI-HarriNeural" },
    "en-Jenny": { lang: "en-US", id: "en-US-JennyNeural" },
    "en-Tony": { lang: "en-US", id: "en-US-TonyNeural" },
  },

  // Preset views
  views: {
    LectureRoom: {
      url: "./assets/views/lecture-room.jpeg",
      type: "image/jpg",
      fi: "Lähikäynti",
    },
  },

  // Preset poses (includes internal poses)
  poses: {
    Straight: { url: "straight", fi: "Suora" },
    Side: { url: "side", fi: "Keno" },
    Hip: { url: "hip", fi: "Lantio" },
    Turn: { url: "turn", fi: "Sivu" },
    Back: { url: "back", fi: "Taka" },
    Wide: { url: "wide", fi: "Haara" },
    OneKnee: { url: "oneknee", fi: "Polvi" },
    TwoKnees: { url: "kneel", fi: "Polvet" },
    Bend: { url: "bend", fi: "Perä" },
    Sitting: { url: "sitting", fi: "Istuva" },
  },

  // Preset gestures
  gestures: {
    HandUp: { name: "handup", fi: "KäsiYlös" },
    OK: { name: "ok" },
    Index: { name: "index", fi: "Etusormi" },
    ThumbUp: { name: "thumbup", fi: "PeukaloYlös" },
    ThumbDown: { name: "thumbdown", fi: "PeukaloAlas" },
    Side: { name: "side", fi: "Sivu" },
    Shrug: { name: "shrug", fi: "Olankohautus" },
    Namaste: { name: "namaste" },
  },

  // Preset animations
  animations: {
    Walking: { url: "./assets/animations/walking.fbx", fi: "Kävely" },
  },

  // Impulse responses
  impulses: {
    Room: { url: "./assets/audio/ir-room.m4a", fi: "Huone" },
    Basement: { url: "./assets/audio/ir-basement.m4a", fi: "Kellari" },
    Forest: { url: "./assets/audio/ir-forest.m4a", fi: "Metsä" },
    Church: { url: "./assets/audio/ir-church.m4a", fi: "Kirkko" },
  },

  // Background ambient sounds/music
  music: {
    Murmur: { url: "./assets/audio/murmur.mp3", fi: "Puheensorina" },
  },
};
