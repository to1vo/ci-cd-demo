![Python CI](https://github.com/to1vo/ci-cd-demo/actions/workflows/ci.yml/badge.svg)<br>
https://github.com/to1vo/ci-cd-demo/actions/workflows/ci.yml

# Python CI demo
- Workflowssa on push ja pull-request triggerit
- Main branch on suojattu suorilta pusheilta, myös bypass oikeuden omaamilta käyttäjiltä.
- Jokaiselle pull request mergelle suoritetaan "Lint, test and package" status check.
- Branchien pitää olla myös ajan tasalla merge vaiheessa. 
- Artifactin tuloksena syntynyt sovellus toimii niinkuin pitää
### Sovelluksen ajaminen
```
python app.py
7
3
warm
```