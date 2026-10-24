import json, random
from pathlib import Path
from datetime import datetime, timedelta

SEED = 20261024
OUT = Path(__file__).resolve().parent
TAGS = ['AI','data-science','programmazione','robotica','cybersecurity','design','UX-UI','arte','fotografia','cinema','musica','teatro','sport','fitness','calcio','basket','running','startup','imprenditoria','marketing','finanza','sostenibilita','ambiente','gaming','networking']
LOCATIONS = ['La Serra','Building 1','Building 2','Building 3','Building 4','Building 5']
FIRST = ['Alex','Andrea','Sam','Nico','Luca','Mia','Noa','Eli','Ari','Leo','Teo','Sasha','Vale','Dani','Rene','Chris','Toni','Ema','Gio','Robin']
LAST = ['Rossi','Bianchi','Verdi','Conti','Moretti','Fontana','Marini','Costa','Ricci','Galli','Serra','Ferri','Greco','Leoni','Riva','Villa','Neri','Colombo','Moro','Fiore']
TITLES = ['Laboratorio pratico','Meetup studenti','Workshop creativo','Sfida a squadre','Talk con ospiti','Sessione introduttiva','Community night','Progetto collaborativo','Mini hackathon','Open lab']
DESCRIPTIONS = ['Un incontro aperto agli studenti per sperimentare, confrontarsi e conoscere nuove persone.', 'Attività guidate e momenti di networking per condividere idee e interessi.', 'Un evento interattivo con esercizi di gruppo e discussione finale.', 'Esperienze pratiche per imparare insieme e costruire connessioni nel campus.']
def write(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
def main():
    rng = random.Random(SEED)
    users=[]
    for i in range(1,41):
        prefs=sorted(rng.sample(TAGS,rng.randint(3,6)))
        users.append({'id':f'usr-{i:03d}','name':f'{FIRST[(i-1)%len(FIRST)]} {LAST[(i-1)//len(FIRST)]}', 'role':'student','preferences':prefs,'year':rng.randint(1,3),'interests_text':f'Mi interessano {", ".join(prefs[:3])} e vorrei conoscere altri studenti con passioni simili.'})
    events=[]
    base=datetime(2026,10,26,16,0)
    for i in range(1,81):
        tags=sorted(rng.sample(TAGS,rng.randint(2,5)))
        start=base+timedelta(days=(i-1)//3, hours=((i-1)%3)*2)
        end=start+timedelta(minutes=rng.choice([60,90,120]))
        events.append({'id':f'evt-{i:03d}','title':f'{TITLES[(i-1)%len(TITLES)]}: {tags[0]}', 'description':f'{DESCRIPTIONS[(i-1)%len(DESCRIPTIONS)]} Focus: {", ".join(tags)}.', 'tags':tags,'location':{'building':LOCATIONS[(i-1)%len(LOCATIONS)]},'start':start.isoformat(timespec='seconds'),'end':end.isoformat(timespec='seconds'),'capacity':rng.choice([15,20,25,30,40,50,60]),'source_id':f'evt-{i:03d}'})
    emails=[]
    for i in range(1,13):
        ev=events[i-1]
        emails.append({'id':f'mail-{i:03d}','from':'eventi@campus.example','to':f'usr-{i:03d}@students.example','subject':f'Invito: {ev["title"]}','body':f'Ciao! Ti segnaliamo {ev["title"]} presso {ev["location"]["building"]}. Vuoi partecipare?','related_event_id':ev['id']})
    write('users.json',users);write('events.json',events);write('emails_mock.json',emails)
    write('tags.json',TAGS)
    schema={'users.json':{'required':['id','name','role','preferences','year','interests_text'],'types':{'id':'string','name':'string','role':'student','preferences':'string[] (3-6)','year':'integer','interests_text':'string'}},'events.json':{'required':['id','title','description','tags','location','start','end','capacity','source_id'],'types':{'id':'string','title':'string','description':'string','tags':'string[] (2-5)','location':{'building':'string','lat':'number (optional)','lng':'number (optional)'},'start':'ISO 8601 local datetime','end':'ISO 8601 local datetime','capacity':'integer','source_id':'string'}},'emails_mock.json':{'required':['id','from','to','subject','body','related_event_id'],'types':{'id':'string','from':'string','to':'string','subject':'string','body':'string','related_event_id':'string'}}}
    write('schema.json',schema)
if __name__=='__main__': main()
