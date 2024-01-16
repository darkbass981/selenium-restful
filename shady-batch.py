import subprocess

# Verify page title
print ("Running shady-title.py")
subprocess.run(["python", "shady-title.py"])

# Verify error if empty form is submitted
print ("Running shady-empty-form.py")
subprocess.run(["python", "shady-empty-form.py"])

# Verify success if filled form is submitted
print ("Running shady-submit-form.py")
subprocess.run(["python", "shady-submit-form.py"])

# Verify error if form is submitted with an empty name field
print ("Running shady-form-empty-name.py")
subprocess.run(["python", "shady-form-empty-name.py"])

# Verify error if form is submitted with an empty email field
print ("Running shady-form-empty-email.py")
subprocess.run(["python", "shady-form-empty-email.py"])

# Verify error if form is submitted with an empty phone field
print ("Running shady-form-empty-phone.py")
subprocess.run(["python", "shady-form-empty-phone.py"])

# Verify error if form is submitted with an empty subject field
print ("Running shady-form-empty-subject.py")
subprocess.run(["python", "shady-form-empty-subject.py"])

# Verify error if form is submitted with a too-short message field
print ("Running shady-form-short-message.py")
subprocess.run(["python", "shady-form-short-message.py"])

# Verify error if form is submitted with a too-short phone field
print ("Running shady-form-short-phone.py")
subprocess.run(["python", "shady-form-short-phone.py"])

# Verify error if form is submitted with a too-long phone field
print ("Running shady-form-long-phone.py")
subprocess.run(["python", "shady-form-long-phone.py"])

# Verify error if form is submitted with a too-long message field
print ("Running shady-form-long-message.py")
subprocess.run(["python", "shady-form-long-message.py"])

# Verify error if form is submitted with an invalid email
print ("Running shady-form-invalid-email.py")
subprocess.run(["python", "shady-form-invalid-email.py"])