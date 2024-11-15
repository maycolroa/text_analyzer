<template>
  <div class="min-h-screen flex flex-col items-center bg-gray-900 text-white p-4">
    <h2 class="text-4xl font-bold mb-6">Aplicación de Análisis de Texto</h2>
    <div class="w-full max-w-md">
      <h3 class="text-2xl font-semibold mb-4">Análisis de Texto</h3>
      <textarea v-model="text" placeholder="Ingresa tu texto aquí"
        class="w-full p-3 h-32 text-gray-800 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none mb-4"></textarea>
      <div class="flex flex-wrap gap-2 mb-6">
        <button @click="analyzeText('word_count')" class="btn bg-blue-500 hover:bg-blue-600">
          Contar Palabras
        </button>
        <button @click="analyzeText('reverse_text')" class="btn bg-green-500 hover:bg-green-600">
          Invertir Texto
        </button>
        <button @click="analyzeText('character_count')" class="btn bg-purple-500 hover:bg-purple-600">
          Contar Caracteres
        </button>
        <button @click="analyzeText('unique_word_count')" class="btn bg-yellow-500 hover:bg-yellow-600">
          Contar Palabras Únicas
        </button>
        <button @click="analyzeText('find_word')" class="btn bg-red-500 hover:bg-red-600">
          Buscar Palabra
        </button>
        <button @click="analyzeText('uppercase')" class="btn bg-indigo-500 hover:bg-indigo-600">
          Texto en Mayúsculas
        </button>
        <button @click="analyzeText('join_list')" class="btn bg-pink-500 hover:bg-pink-600">
          Unir Lista
        </button>
        <button @click="analyzeText('replace_words')" class="btn bg-teal-500 hover:bg-teal-600">
          Reemplazar Palabras
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
        <p v-if="analysisResult.uppercase_text" class="mb-2"><strong>Texto en mayúsculas:</strong> {{
          analysisResult.uppercase_text }}</p>
        <p v-if="analysisResult.joined_text" class="mb-2"><strong>Texto unido:</strong> {{ analysisResult.joined_text }}
        </p>
        <p v-if="analysisResult.replaced_text" class="mb-2"><strong>Texto reemplazado:</strong> {{
          analysisResult.replaced_text }}</p>
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
        } else if (operation === 'join_list') {
          const inputList = prompt("Ingresa los elementos de la lista separados por comas:");
          payload.list_to_join = inputList ? inputList.split(",").map(item => item.trim()) : [];
        } else if (operation === 'replace_words') {
          payload.toReplace = prompt("Ingresa la palabra que quieres reemplazar:");
          payload.replacement = prompt(`Ingresa la palabra por la que quieres reemplazar "${payload.toReplace}":`);
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

<style scoped>
.btn {
  padding: 0.5rem 1rem;
  color: white;
  border-radius: 0.375rem;
  font-weight: 500;
  transition: background-color 0.3s ease;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
