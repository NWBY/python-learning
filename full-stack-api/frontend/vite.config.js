import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  define: {
    apiUrl: JSON.stringify('http://localhost:5000')
  },
  plugins: [vue()]
})
