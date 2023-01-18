#### What
Please provide a short description of the changes in this merge request.

#### Why
Explain why the proposed change is necessary.

`Story`: https://jira-olist.atlassian.net/browse/XXX-###

`Task`: https://jira-olist.atlassian.net/browse/XXX-###

---

#### Reminders
- Tests have been added and are passing ([`make lint`](Makefile)`&&`[`make test`](Makefile)). (If you've fixed a bug or added a new feature)
- The [`coding guidelines`] have been followed.
- All env vars used (if any) have been added to:
  - [`local.env`](local.env)
  - [`.gitlab-ci.yml`](.gitlab-ci.yml)
  - SecretsManager (You can add them, even when the MR has not been merged yet)
- Dependencies are up to date.
- Required schema/data changes are reflected in migrations.
- Review your own code before submitting the merge request.
- Confirm [CI build] is successfull before opening the merge request.
- If any changes have been made to a public endpoint, update [documentation] and the [api gateway].
- Verify if has new migrations for third party libs
- If there are new migrations, run the migrations locally and measure completion time with a newly downloaded and restored database, including historical data, following procedures on [checklist migration]
- If necessary add new translation messages (pt-br) on `django.mo` and `django.po` following procedures on [translation process]


[CI build]: https://gitlab.olist.io/su_finance/payments-api/-/pipelines
[`coding guidelines`]: https://jira-olist.atlassian.net/wiki/spaces/OP/pages/52461580/0008+-+Diretrizes+de+Estilo+de+C+digo+Python
[api gateway]: https://github.com/olist/forehead
[documentation]: https://dev.olist.com/
[translation process]: https://jira-olist.atlassian.net/wiki/spaces/OP/pages/261685261/Processo+de+Tradu+o+das+Apps
[checklist migration]: https://jira-olist.atlassian.net/wiki/spaces/OP/pages/430145544/Checklist+Migration
