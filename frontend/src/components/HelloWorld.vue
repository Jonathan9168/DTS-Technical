<template>
  <div class="container">
    <h2>Create Note</h2>

    <form @submit.prevent="createNote">
      <label>Title</label>
      <input v-model="title" />

      <label>Description</label>
      <textarea v-model="description"></textarea>

      <label>Due Date</label>
      <input type="datetime-local" v-model="dueDateTime" />

      <label>Status</label>
      <input type="checkbox" v-model="status" />

      <button type="submit">Create Note</button>
    </form>

    <div v-if="successMessage" class="success">
      {{ successMessage }}

      <div class="created-note">
        <h3>Created Note</h3>
        <div class="note-row"><strong>ID:</strong> {{ createdNote.id }}</div>
        <div class="note-row">
          <strong>Title:</strong> {{ createdNote.title }}
        </div>
        <div class="note-row">
          <strong>Description:</strong> {{ createdNote.description }}
        </div>
        <div class="note-row">
          <strong>Status:</strong>
          {{ createdNote.status ? "Completed" : "Pending" }}
        </div>
        <div class="note-row">
          <strong>Due Date:</strong> {{ createdNote.due_date_time }}
        </div>
        <div class="note-row">
          <strong>Created At:</strong> {{ createdNote.created_at }}
        </div>
      </div>
    </div>

    <!-- Error message -->
    <div v-if="errorMessage" class="error">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const title = ref("");
const description = ref("");
const status = ref(false);
const dueDateTime = ref("");

const successMessage = ref("");
const errorMessage = ref("");
const createdNote = ref(null);

async function createNote() {
  successMessage.value = "";
  errorMessage.value = "";
  createdNote.value = null;

  const payload = {
    title: title.value,
    description: description.value,
    status: status.value,
    due_date_time: dueDateTime.value,
  };

  try {
    const res = await fetch("http://127.0.0.1:8000/dts_app/notes/create/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await res.json();

    if (res.ok) {
      successMessage.value = "Note created successfully!";
      createdNote.value = data;

      title.value = "";
      description.value = "";
      status.value = false;
      dueDateTime.value = "";
    } else {
      errorMessage.value = data.error || "An error occurred.";
    }
  } catch (err) {
    errorMessage.value = "Failed to reach the server.";
  }
}
</script>

<style scoped>
* {
  font-family: system-ui, Avenir, Helvetica, Arial, sans-serif;
}

.container {
  max-width: 400px;
  margin: auto;
  font-family: Arial;
}

input,
textarea {
  width: 100%;
  margin-bottom: 10px;
  padding: 8px;
}

button {
  padding: 8px 15px;
}

.success {
  color: rgb(131, 241, 131);
  margin-top: 5%;
}

.error {
  color: rgb(228, 91, 91);
  margin-top: 5%;
}

.created-note {
  padding: 5%;
  background: #333;
  border-radius: 8px;
  width: 100%;
  margin-top: 5%;
}

.created-note h3 {
  text-align: center;
  padding: 0;
  margin-top: 0%;

}

.note-row {
  margin: 4px 0;
  padding: 0;
  line-height: 1.2;
  display: flex;
  gap: 6px;
}

.note-item {
  margin: 1%;
  padding: 0;
}

.note-row strong {
  margin: 0;
  padding: 0;
}
</style>
