<template>
  <div
    class="flex flex-col justify-center items-center gap-3 w-screen h-screen overflow-auto bg-linear-to-r from-gray-100 to-gray-300">

    <h1 class="text-3xl font-bold">AI Text Summarizer</h1>

    <div class="flex flex-col gap-3 w-[50%] p-6 shadow-md rounded-2xl bg-white">

      <div class="flex flex-col items-end gap-3">
        <textarea v-model="text"
          class="w-full h-[60px] max-h-[300px] p-3 resize-none overflow-y-auto rounded-lg bg-gray-100"
          oninput="this.style.height='auto'; this.style.height=this.scrollHeight+'px'"
          placeholder="Type a prompt and let AI to summerize it for you"></textarea>

        <button @click="summarize" :disabled="loading"
          :class="[loading ? 'opacity-50 pointer-events-none' : '', 'flex w-fit px-3 py-2 rounded-2xl text-lg font-medium cursor-pointer text-white bg-linear-to-r from-purple-600 to-fuchsia-600']">
          Summerize
        </button>

      </div>

      <!--  --- Summary Section --- -->
      <div v-if="summary" class="flex flex-col gap-2 max-h-[300px] overflow-auto p-2">
        <h2 class="text-lg font-semibold">Summary:</h2>
        <p>{{ summary }}</p>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'
const text = ref('')
const summary = ref('')
const loading = ref(false);

async function summarize() {
  loading.value = true;
  summary.value = 'Thinking...';

  const res = await fetch('http://localhost:8000/api/summarize/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: text.value })
  })
  const data = await res.json()
  summary.value = data.summary || data.error
  loading.value = false;
}
</script>
