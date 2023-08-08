% rebase('base.tpl')


<div class="position-static">

        <div class="position-absolute top-50 start-50 translate-middle">
                
                <form class="p-3 border border-dark" method="get" action="/results">
                        <label for="actor_1">Schauspieler*in 1</label>
                        <input type="text" name="person_1" id="actor_1" class="rounded-0 m-1" placeholder="Amanda Blake" list="person_1_datalist">
                        <br>
                        <label for="actor_2">Schauspieler*in 2</label>
                        <input type="text" name="person_2" id="actor_2" class="rounded-0 m-1" placeholder="James Arness" list="person_2_datalist">
                        <br>
                        <br>
                        <input type="submit" value="Suchen" class="btn btn-primary rounded-0">
                        <input type="reset" value="Löschen" class="btn btn-outline-danger rounded-0">

                </form>

                
                <p class=""> <h2 class="h-6">Beschreibung </h2>
                        Hier können Namen von 2 Schauspieler*innen angegeben werden um zu schauen in welchen Produktionen sie zusammengearbeitet haben.
                        Dieser Prototype verwendet Produktionen aus den <b>1950er Jahren</b>.<br> 
                        Für diese Anwendung muss der Name genau angegeben werden: 
                        <ul>
                        <li>Groß-/Kleinschreibung</li>
                        <li>keine Leerzeichen vor und nach nach dem Namen</li>
                        </ul>
                </p>

        </div>
</div>

