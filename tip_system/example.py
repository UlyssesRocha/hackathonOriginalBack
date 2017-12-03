import gen_tips, retrieve

# mocked: this info is retrieved from the person's bank account
pcts,_ = gen_tips.get_pcts()
print(retrieve.get_tip(pcts))
