# -*- coding: utf-8
from odoo import http
from odoo.http import request


class StudentRegistration(http.Controller):
    @http.route(['/register'], type='http', auth="public",website=True)
    def website_menu(self):
        # request.env['hostel.student'].sudo().create()
        
        return request.render("hostel_management.register_form")
    
    @http.route(['/register_submit'], type='http', auth="public", website=True)
    def website_menu_student(self, **post):
        request.env['hostel.student'].create(post)
        return request.render('hostel_management.registration_success_template1')


class ServiceRequest(http.Controller):

    @http.route(['/complaint'], type='http', auth="public",website=True)
    def complaint_form(self):   
        return request.render("hostel_management.complaint_registration_form")

    @http.route(['/complaint_submit'], type='http', auth="public",website=True,csrf=False)
    def complaint_submission(self,**post):
        name=post.get('student_id')
        complaint=post.get('complaint_description')
        if request.env['hostel.student'].search([('sequence','=',name)]):
            student_id = request.env['hostel.student'].search([('sequence','=',name)])
            request.env['hostel.helpdesk'].create({
            'student_id':student_id.id,'complaint_description':complaint,
            })
            return request.render('hostel_management.registration_success_template')
        else :
            return request.render('hostel_management.registration_invalid_template')


        

    
    
class Home(http.Controller):
    @http.route(['/'], type='http', auth='public', website=True)
    def home(self):
        return http.request.render('hostel_management.home',{})
                            


class ContactUs(http.Controller):
    @http.route(['/contact'], type='http', auth="public", website=True)
    def contact_menu(self):        
        return request.render("hostel_management.contact_form")
    
    @http.route(['/contact_submit'], type='http', auth="public", website=True)
    def website_success_contact(self, **post):
        request.env['hostel.contact'].create(post)
        return request.render('hostel_management.contact_success_template')
