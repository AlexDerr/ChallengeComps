<template>
  <div style="text-align: center;">
    <h1> Challenge Comps </h1>
    <div style="margin-bottom: 10px;">
      <select v-model="champ1">
        <option v-for="value, key in allChampDict"> {{key}} </option>
      </select>
      <select v-model="champ2">
        <option v-for="value, key in allChampDict"> {{key}} </option>
      </select>
      <select v-model="champ3">
        <option v-for="value, key in allChampDict"> {{key}} </option>
      </select>
      <select v-model="champ4">
        <option v-for="value, key in allChampDict"> {{key}} </option>
      </select>
      <select v-model="champ5">
        <option v-for="value, key in allChampDict"> {{key}} </option>
      </select>
    </div>
    <div v-for="challenge in challengeDict" v-bind:class="['challenge-block', challenge['count'] >= challenge['req'] ? 'meet-req' : 'not-req']">
      <span class="inline-block" style="margin-right: auto">
        {{ challenge['name'] }} : {{ challenge['count']}} / {{ challenge['req'] }}
      </span>
    </div>
  </div>
</template>

<script lang="ts">
  export default defineComponent({
    computed: {
      challengeDict() {
        let temp = [].concat(this.allChampDict[this.champ1], this.allChampDict[this.champ2], this.allChampDict[this.champ3], this.allChampDict[this.champ4], this.allChampDict[this.champ5])
        let counts = {}
        temp.forEach(item => {
          if(counts[item] != undefined){
            counts[item] += 1;
          }
          else if(item != undefined){
            counts[item] = 1
          }
        });

        let challengesDict = {
          'aoe': { name: 'It Has "Ultimate In the Name!', count: 0, req: 3},
          'heal': { name: 'We Protec', count: 0, req: 3},
          'poke': { name: 'We\'re Good Over Here', count: 0, req: 3},
          'displacement': { name: 'Get Over Here', count: 0, req: 3},
          'globals': { name: 'Nowhere to Hide', count: 0, req: 3},
          'revive': { name: 'They Just... Don\'t... DIE!', count: 0, req: 3},
          'immobilizing': { name: 'Hold That Pose', count: 0, req: 3},
          'stealth': { name: 'Where\'d They Go?', count: 0, req: 3},
          'summon': { name: 'Summoners on the Rift', count: 0, req: 5},
          'trap': { name: 'It\'s a Trap!', count: 0, req: 3},
          'terrain': { name: 'I\'m Helping', count: 0, req: 3},
          'shurima': { name: 'The Sun Disc Never Sets', count: 0, req: 5},
          'ionia': { name: 'Everybody was Wuju Fighting', count: 0, req: 5},
          'bandle': { name: ' 5 under 5\'', count: 0, req: 5},
          'bilgewater': { name: 'All Hands on Deck', count: 0, req: 5},
          'demacia': { name: 'FOR DEMACIA', count: 0, req: 5},
          'freljord': { name: 'Ice, Ice, Baby', count: 0, req: 5},
          'ixtal': { name: 'Elemental, My Dear Watson', count: 0, req: 5},
          'noxus': { name: 'Strength Above All', count: 0, req: 5},
          'piltover': { name: 'Calculated', count: 0, req: 5},
          'shadowIsles': { name: 'Spooky Scary Skeletons', count: 0, req: 5},
          'targon': { name: 'Peak Performance', count: 0, req: 5},
          'void': { name: '(Inhuman Screeching Sounds)', count: 0, req: 5},
          'zaun': { name: 'Chemtech Comrades', count: 0, req: 5},
        };

        for(let challenge in challengesDict){
          challengesDict[challenge]['count'] = counts[challenge] == undefined ? 0 : counts[challenge]
        }
        return challengesDict;
      }
    },
    watch: {},
    mounted() {},
    unmounted() {},
    methods: {},

    data() {
      return {
        champ1: 'AurelionSol',
        champ2: 'Bard',
        champ3: 'Galio',
        champ4: 'Maokai',
        champ5: 'Alistar',

        allChampDict : {
          Aatrox: ['immobilizing'],
          Ahri: ['ionia'],
          Akali: ['stealth', 'ionia'],
          Akshan: ['poke', 'globals', 'revive', 'stealth', 'shurima'],
          Alistar: ['heal', 'displacement', 'revive', 'immobilizing'],
          Amumu: ['aoe', 'immobilizing', 'shurima'],
          Anivia: ['revive', 'immobilizing', 'terrain', 'freljord'],
          Annie: ['aoe', 'heal', 'summon'],
          Aphelios: ['targon'],
          Ashe: ['poke', 'globals', 'freljord'],
          AurelionSol: ['aoe', 'displacement', 'immobilizing', 'targon'],
          Azir: ['aoe', 'poke', 'displacement', 'summon', 'terrain', 'shurima'],
          Bard: ['aoe', 'heal', 'globals', 'revive', 'immobilizing'],
          BelVeth: ['aoe', 'revive', 'void'],
          Blitzcrank: ['aoe', 'displacement', 'immobilizing', 'zaun'],
          Brand: [],
          Braum: ['aoe', 'revive', 'immobilizing', 'freljord'],
          Caitlyn: ['poke', 'globals', 'trap', 'piltover'],
          Camille: ['immobilizing', 'piltover'],
          Cassiopeia: ['aoe', 'noxus'],
          ChoGath: ['poke', 'void'],
          Corki: ['aoe', 'poke', 'bandle', 'piltover'],
          Darius: ['displacement', 'noxus'],
          Diana: ['aoe', 'targon'],
          DrMundo: ['poke', 'zaun'],
          Draven: ['aoe', 'globals', 'noxus'],
          Ekko: ['aoe', 'revive', 'zaun'],
          Elise: ['revive', 'summon', 'shadowIsles'],
          Evelynn: ['revive', 'stealth', 'shadowIsles'],
          Ezreal: ['aoe', 'poke', 'globals', 'piltover'],
          Fiddlesticks: ['aoe', 'summon', 'shadowIsles'],
          Fiora: ['heal', 'revive', 'demacia'],
          Fizz: ['aoe', 'revive', 'bandle', 'bilgewater'],
          Galio: ['aoe', 'heal', 'globals', 'immobilizing', 'demacia'],
          Gangplank: ['aoe', 'poke', 'globals', 'trap', 'bilgewater'],
          Garen: ['demacia'],
          Gnar: ['aoe', 'displacement', 'immobilizing', 'bandle', 'freljord'],
          Gragas: ['aoe', 'displacement', 'immobilizing', 'freljord'],
          Graves: ['aoe', 'bilgewater'],
          Gwen: ['revive', 'shadowIsles'],
          Hecarim: ['aoe', 'displacement', 'immobilizing', 'shadowIsles'],
          Heimerdinger: ['aoe', 'summon', 'bandle', 'piltover'],
          Illaoi: ['aoe', 'summon', 'bilgewater'],
          Irelia: ['terrain', 'ionia'],
          Ivern: ['heal', 'immobilizing', 'summon', 'terrain', 'ionia'],
          Janna: ['aoe', 'heal', 'displacement', 'immobilizing', 'zaun'],
          JarvanIV: ['aoe', 'immobilizing', 'terrain', 'demacia'],
          Jax: ['revive'],
          Jayce: ['poke', 'displacement', 'piltover'],
          Jhin: ['poke', 'globals', 'trap', 'ionia'],
          Jinx: ['aoe', 'poke', 'globals', 'trap', 'zaun'],
          KaiSa: ['poke', 'globals', 'stealth', 'void'],
          Kalista: ['revive', 'summon', 'shadowIsles'],
          Karma: ['heal', 'poke', 'ionia'],
          Karthus: ['aoe', 'globals', 'revive', 'shadowIsles'],
          Kassadin: ['void'],
          Katarina: ['aoe', 'noxus'],
          Kayle: ['aoe', 'heal', 'revive', 'demacia'],
          Kayn: ['revive', 'ionia'],
          Kennen: ['aoe', 'ionia', 'bandle'],
          KhaZix: ['stealth', 'void'],
          Kindred: ['heal', 'revive', 'summon'],
          Kled: ['poke', 'displacement', 'globals', 'revive', 'bandle', 'noxus'],
          KogMaw: ['poke', 'revive', 'void'],
          LeBlanc: ['stealth', 'noxus'],
          LeeSin: ['heal', 'displacement', 'ionia'],
          Leona: ['aoe', 'targon'],
          Lillia: ['globals', 'ionia'],
          Lissandra: ['aoe', 'revive', 'summon', 'freljord'],
          Lucian: ['demacia'],
          Lulu: ['heal', 'bandle'],
          Lux: ['aoe', 'heal', 'poke', 'globals', 'demacia'],
          Malphite: ['aoe', 'ixtal'],
          Malzahar: ['revive', 'summon', 'void'],
          Maokai: ['aoe', 'poke', 'displacement', 'globals', 'revive', 'summon', 'trap', 'shadowIsles'],
          MasterYi: ['revive', 'ionia'],
          MissFortune: ['aoe', 'bilgewater'],
          Mordekaiser: ['displacement'],
          Morgana: ['aoe', 'heal', 'demacia'],
          Nami: ['aoe', 'heal'],
          Nasus: ['shurima'],
          Nautilus: ['displacement', 'bilgewater'],
          Neeko: ['aoe', 'stealth', 'summon', 'ixtal'],
          Nidalee: ['heal', 'poke', 'trap', 'ixtal'],
          Nocturne: ['globals', 'stealth'],
          NunuWillump: ['aoe', 'freljord'],
          Olaf: ['revive', 'freljord'],
          Orianna: ['aoe', 'heal', 'displacement', 'summon', 'piltover'],
          Ornn: ['aoe', 'terrain', 'freljord'],
          Pantheon: ['aoe', 'poke', 'globals', 'revive', 'targon'],
          Poppy: ['displacement', 'bandle', 'demacia'],
          Pyke: ['displacement', 'stealth', 'bilgewater'],
          Qiyana: ['aoe', 'stealth', 'ixtal'],
          Quinn: ['demacia'],
          Rakan: ['aoe', 'heal', 'revive', 'ionia'],
          Rammus: ['aoe', 'shurima'],
          RekSai: ['void'],
          Rell: ['aoe', 'heal', 'displacement', 'noxus'],
          RenataGlasc: ['aoe', 'heal', 'revive', 'zaun'],
          Renekton: ['shurima'],
          Rengar: ['stealth', 'ixtal'],
          Riven: ['aoe', 'noxus'],
          Rumble: ['aoe', 'bandle'],
          Ryze: ['globals'],
          Samira: ['aoe', 'noxus'],
          Sejuani: ['aoe', 'freljord'],
          Senna: ['aoe', 'heal', 'poke', 'globals', 'stealth', 'shadowIsles'],
          Seraphine: ['aoe', 'heal', 'poke', 'piltover'],
          Sett: ['aoe', 'displacement', 'ionia'],
          Shaco: ['stealth', 'summon', 'trap'],
          Shen: ['heal', 'globals', 'ionia'],
          Shyvana: ['poke', 'demacia'],
          Singed: ['displacement', 'zaun'],
          Sion: ['globals', 'revive', 'noxus'],
          Sivir: ['poke', 'shurima'],
          Skarner: ['displacement', 'shurima'],
          Sona: ['aoe', 'heal', 'demacia'],
          Soraka: ['heal', 'globals', 'targon'],
          Swain: ['aoe', 'displacement', 'globals', 'noxus'],
          Sylas: ['demacia'],
          Syndra: ['ionia'],
          TahmKench: ['heal', 'displacement', 'revive', 'bilgewater'],
          Taliyah: ['poke', 'displacement', 'globals', 'terrain', 'shurima'],
          Talon: ['aoe', 'stealth', 'noxus'],
          Taric: ['heal', 'revive', 'targon'],
          Teemo: ['stealth', 'trap', 'bandle'],
          Thresh: ['heal', 'displacement', 'shadowIsles'],
          Tristana: ['displacement', 'bandle'],
          Trundle: ['terrain', 'freljord'],
          Tryndamere: ['revive', 'freljord'],
          TwistedFate: ['poke', 'globals', 'bilgewater'],
          Twitch: ['aoe', 'stealth', 'zaun'],
          Udyr: ['freljord'],
          Urgot: ['displacement', 'zaun'],
          Varus: ['poke', 'ionia'],
          Vayne: ['displacement', 'stealth', 'demacia'],
          Veigar: ['terrain', 'bandle'],
          VelKoz: ['aoe', 'poke', 'void'],
          Vex: ['poke', 'globals', 'bandle'],
          Vi: ['piltover'],
          Viego: ['stealth', 'shadowIsles'],
          Viktor: ['aoe', 'poke', 'zaun'],
          Vladimir: ['aoe', 'revive', 'noxus'],
          Volibear: ['aoe', 'freljord'],
          Warwick: ['zaun'],
          Wukong: ['ionia'],
          Xayah: ['aoe', 'poke', 'ionia'],
          Xerath: ['poke', 'globals', 'shurima'],
          XinZhao: ['aoe', 'displacement', 'revive', 'demacia'],
          Yasuo: ['ionia'],
          Yone: ['aoe', 'displacement', 'ionia'],
          Yorick: ['summon', 'terrain', 'shadowIsles'],
          Yuumi: ['aoe', 'heal', 'poke', 'revive', 'bandle'],
          Zac: ['aoe', 'displacement', 'revive', 'zaun'],
          Zed: ['revive', 'summon', 'ionia'],
          Zeri: ['zaun'],
          Ziggs: ['aoe', 'poke', 'displacement', 'globals', 'trap', 'bandle', 'zaun'],
          Zilean: ['heal', 'revive', 'shurima'],
          Zoe: ['poke', 'targon'],
          Zyra: ['aoe', 'summon', 'trap', 'ixtal'],
        }
      }
    },
  })
</script>

<style>
  .challenge-block {
    width: 23%;
    display: inline-block;
    border: 1px solid black;
    padding: 10px;
    text-align: left;
  }

  .meet-req {
    background-color:rgb(14, 179, 55);
  }

  .not-req {
    background-color:rgb(189, 18, 18);
  }
</style>