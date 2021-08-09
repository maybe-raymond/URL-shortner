"""
def Custom():
    if form.validate_on_submit():
        U = URL(orginal_link =form.url.data,  new_link=form.custom.data)
        db.session.add(U)
        db.session.commit()
        return redirect(url_for("New_url", new=form.custom.data))
    return render_template("custom.html", form=form)


@app.route("/New url/", methods=["POST", "GET"])
def New_url():
    form = Url_form()
    new = request.args.get("new")
    form.url.data = f"{domain}{new}"
    return render_template("r.html", form=form)

"""