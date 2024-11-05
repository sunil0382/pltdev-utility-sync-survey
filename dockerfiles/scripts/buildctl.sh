

CGO_ENABLED=0 go build -ldflags="-s -w -X 'github.com/eand-iot/pltdev-utility-sync-survey/ctl/version.Version=$(git rev-parse --short HEAD)' -X 'github.com/eand-iot/pltdev-utility-sync-survey/ctl/version.CommitHash=$(git rev-parse HEAD)' -X 'github.com/eand-iot/pltdev-utility-sync-survey/ctl/version.BuildTime=$(date -u "+%Y-%m-%dT%H:%M:%SZ")'" -o ./bin/surveyctl ./ctl/main.go

if [ ! -d ~/pltdev-utility-sync-survey/bin ]; then
  mkdir -p ~/pltdev-utility-sync-survey/bin
fi


cp ./bin/surveyctl ~/pltdev-utility-sync-survey/bin/surveyctl

printf "\n\n✅ Installation complete.\n"

printf  "Add the following to your bash \n\n\texport PATH=\"\$HOME/pltdev-utility-sync-survey/bin:\$PATH\"\n\n"
