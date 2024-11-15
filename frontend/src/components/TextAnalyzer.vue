<template>
  <div class="min-h-screen flex flex-col items-center bg-gray-900 text-white p-4">
    <h2 class="text-4xl font-bold mb-6">Aplicación de Análisis de Texto</h2>
    <div class="w-full max-w-md">
      <h3 class="text-2xl font-semibold mb-4">Análisis de Texto</h3>
      <textarea v-model="text" placeholder="Ingresa tu texto aquí"
        class="w-full p-3 h-32 text-gray-800 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none mb-4"></textarea>
      <div class="flex flex-wrap gap-2 mb-6">
        <button @click="analyzeText('word_count')"
          class="px-4 py-2 bg-blue-500 hover:bg-blue-600 focus:ring-2 focus:ring-blue-500 rounded-md shadow-md transition ease-in-out duration-300">
          Contar Palabras
        </button>
        <button @click="analyzeText('reverse_text')"
          class="px-4 py-2 bg-green-500 hover:bg-green-600 focus:ring-2 focus:ring-green-500 rounded-md shadow-md transition ease-in-out duration-300">
          Invertir Texto
        </button>
        <button @click="analyzeText('character_count')"
          class="px-4 py-2 bg-purple-500 hover:bg-purple-600 focus:ring-2 focus:ring-purple-500 rounded-md shadow-md transition ease-in-out duration-300">
          Contar Caracteres
        </button>
        <button @click="analyzeText('unique_word_count')"
          class="px-4 py-2 bg-yellow-500 hover:bg-yellow-600 focus:ring-2 focus:ring-yellow-500 rounded-md shadow-md transition ease-in-out duration-300">
          Contar Palabras Únicas
        </button>
        <button @click="analyzeText('find_word')"
          class="px-4 py-2 bg-red-500 hover:bg-red-600 focus:ring-2 focus:ring-red-500 rounded-md shadow-md transition ease-in-out duration-300">
          Buscar Palabra
        </button>
      </div>

      <div v-if="analysisResult" class="bg-gray-800 p-4 rounded-md shadow-lg">
        <h3 class="text-xl font-semibold mb-2">Resultados:</h3>
        <p v-if="analysisResult.word_count" class="mb-2"><strong>Conteo de palabras:</strong> {{
          analysisResult.word_count }}</p>
        <p v-if="analysisResult.reversed_text" class="mb-2"><strong>Texto al revés:</strong> {{
          analysisResult.reversed_text }}</p>
        <p v-if="analysisResult.character_count" class="mb-2"><strong>Conteo de caracteres:</strong> {{
          analysisResult.character_count }}</p>
        <p v-if="analysisResult.unique_word_count" class="mb-2"><strong>Conteo de palabras únicas:</strong> {{
          analysisResult.unique_word_count }}</p>
        <div v-if="analysisResult.word_locations">
          <h4 class="text-lg font-semibold mt-4">Ubicaciones de cada palabra:</h4>
          <ul class="list-disc list-inside">
            <li v-for="(locations, word) in analysisResult.word_locations" :key="word" class="ml-4">
              {{ word }}: {{ locations }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      text: "",
      analysisResult: null,
    };
  },
  methods: {
    async analyzeText(operation) {
      try {
        const payload = { text: this.text, operation };
        if (operation === 'find_word') {
          payload.word = prompt("Ingresa la palabra a buscar:");
        }
        const response = await axios.post(`${import.meta.env.VITE_API_URL}/analyze`, payload);
        this.analysisResult = response.data;
      } catch (error) {
        console.error("Error al analizar el texto:", error);
      }
    }
  }
};
</script>

<style scoped></style>
