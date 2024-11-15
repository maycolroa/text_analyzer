# Etapa de construcción
FROM node:18 AS build-stage

WORKDIR /app

COPY package*.json ./

# Instala las dependencias, incluyendo axios
RUN npm install

COPY . .

RUN npm run build

# Etapa de producción
FROM nginx:alpine AS production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

