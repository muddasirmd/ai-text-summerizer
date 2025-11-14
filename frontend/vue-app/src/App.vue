<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center p-6">
    <h1 class="text-2xl font-bold mb-4">AI Text Summarizer</h1>
    <textarea v-model="text" class="w-full max-w-lg p-3 rounded border" rows="8" placeholder="Paste your text here..."></textarea>
    <button @click="summarize" class="bg-blue-500 text-white px-4 py-2 rounded mt-3">Summarize</button>
    <div v-if="summary" class="mt-4 bg-white shadow p-4 rounded w-full max-w-lg">
      <h2 class="font-semibold mb-2">Summary:</h2>
      <p>{{ summary }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const text = ref('')
const summary = ref('')

async function summarize() {
  const res = await fetch('http://localhost:8000/api/summarize/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: text.value })
  })
  const data = await res.json()
  summary.value = data.summary || data.error
}
</script>
