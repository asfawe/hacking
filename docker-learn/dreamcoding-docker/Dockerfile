FROM node:16-alpine

# 우리가 작업할 공간
WORKDIR /app

# 우리 프로젝트 파일들을 복사해야 함.
COPY package.json package-lock.json ./


# npm install 대신 npm ci를 사용하는 이유는 예를들어 package.json에서 3.0 이상 버전은 다 괜찮다 라고 명시를 해두면

# npm install로 다운로드 했을 때 package.json에서 install할 패키지중에 5.0이 나온 패키지가 있다면 npm install은 그걸 설치하게 됩니다.

# 하지만 npm ci로 패키지들을 설치하게 되면 package.json이 아닌 package-lock.json을 기준으로 설치하기 때문에 npm ci를 사용합니다.

RUN npm ci

# 제일 많이 변경 되는 놈을 제일 끝에 작성해야 합니다.
COPY index.js ./
# node index.js를 실행할거다.
ENTRYPOINT [ "node", "index.js" ]

