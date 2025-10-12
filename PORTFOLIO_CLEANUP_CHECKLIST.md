# Portfolio Cleanup Checklist - Remove Onboarding Framework

## ✅ **Pre-Removal Checklist**

### **1. Backup Files**
- [ ] Create `archive/` directory in your portfolio
- [ ] Copy `projects/onboarding-framework.html` to `archive/onboarding-framework.html`
- [ ] Verify backup was created successfully

### **2. Remove Project File**
- [ ] Delete `projects/onboarding-framework.html`
- [ ] Verify file is completely removed

## ✅ **Update Portfolio Files**

### **3. Main Portfolio Page (index.html or main page)**
- [ ] Open main portfolio page in editor
- [ ] Find and remove Onboarding Framework project section
- [ ] Remove any links to `projects/onboarding-framework.html`
- [ ] Remove project description and preview
- [ ] Save changes

### **4. Navigation Menu**
- [ ] Check navigation menu for Onboarding Framework link
- [ ] Remove from featured projects menu
- [ ] Remove from any project grid or list
- [ ] Update any project counters

### **5. Other References**
- [ ] Search entire portfolio for "onboarding-framework.html" references
- [ ] Remove any cross-references or mentions
- [ ] Check for any hardcoded links in CSS or JavaScript

## ✅ **Testing & Validation**

### **6. Test Portfolio**
- [ ] Open portfolio in browser
- [ ] Check all navigation links work
- [ ] Verify no broken links or 404 errors
- [ ] Test on different devices/browsers
- [ ] Check that project count is accurate

### **7. SEO Considerations**
- [ ] Update sitemap.xml if you have one
- [ ] Check Google Search Console for any indexing issues
- [ ] Consider adding 301 redirect if the page had good SEO value

## ✅ **Post-Removal Benefits**

### **8. Verify Improvements**
- [ ] Portfolio looks cleaner and more focused
- [ ] No duplicate or overlapping projects
- [ ] Hybrid Project Management System is prominently featured
- [ ] Navigation is simpler and clearer

## 🎯 **Files to Check/Update**

### **Main Files:**
- [ ] `index.html` (main portfolio page)
- [ ] Navigation menu files
- [ ] CSS files (for any project-specific styling)
- [ ] JavaScript files (for project counters or dynamic content)

### **Potential Locations:**
- [ ] Header navigation
- [ ] Featured projects section
- [ ] Project grid or list
- [ ] Footer links
- [ ] About page (if it mentions projects)

## 📋 **Quick Commands (if using command line)**

```bash
# 1. Backup
mkdir -p archive
cp projects/onboarding-framework.html archive/

# 2. Remove
rm projects/onboarding-framework.html

# 3. Search for references (optional)
grep -r "onboarding-framework" . --exclude-dir=archive
grep -r "Onboarding Framework" . --exclude-dir=archive
```

## 🚨 **Important Notes**

- **Test thoroughly** before making changes live
- **Keep the backup** in archive folder
- **Check all pages** of your portfolio, not just the main page
- **Update any external links** that might point to the removed page

## 🎉 **Expected Result**

After cleanup, your portfolio should have:
- ✅ One comprehensive Hybrid Project Management System
- ✅ No duplicate or overlapping capabilities
- ✅ Cleaner, more focused presentation
- ✅ Clear value proposition for visitors
- ✅ Better showcase of your evolution and improvement

---

**Complete this checklist and your portfolio will be streamlined and focused on your best work!**
