# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
import logging


class ResPartner(models.Model):
    _inherit = "mrp.production"

    def button_mark_done(self):

        #Funcionalidad de cambiar el coste por la suma de los costes

        logging.info("*******************| mark done |*********************")

        #Variables
        coste_total = 0
        pvp_total = 0
        product_id = self.product_id
        lines = self.move_raw_ids
        logging.info("*******************| Producto |*********************")
        logging.info(product_id.name)

        logging.info("*******************|  materiales  |*********************")

        for line in lines:

            logging.info("*******************|  materiales  |*********************")
            logging.info(line.product_id.name)

            logging.info("*******************|  cantidad  |*********************")
            logging.info(line.product_qty)

            logging.info("*******************|  coste/U  |*********************")
            logging.info(line.product_id.standard_price)

            coste= line.product_id.standard_price * line.product_qty

            logging.info("*******************|  coste  |*********************")
            logging.info(coste)

            logging.info("*******************|  PVP/U  |*********************")
            logging.info(line.product_id.list_price)

            pvp = line.product_id.list_price * line.product_qty

            logging.info("*******************|  PVP  |*********************")
            logging.info(pvp)


            coste_total= coste_total + coste
            pvp_total=pvp_total + pvp

        logging.info("*******************|  coste total  |*********************")
        logging.info( coste_total )

        logging.info("*******************|  pvp total  |*********************")
        logging.info(pvp_total)

        #llamada a la función button_mak_done de la clase padre
        resultado = super().button_mark_done()

        return resultado
