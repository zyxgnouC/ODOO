/** @odoo-module **/
import options from "@web_editor/js/editor/snippets.options";
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToFragment } from "@web/core/utils/render";

options.registry.SpecialManualProduct = options.Class.extend({
    /**
     * @override
     */
    init: function () {
        this._super.apply(this, arguments);
        this.productManualCategories = [];
    },
    /**
     * @override
     */
    async willStart() {
        const _super = this._super.bind(this);
        return _super(...arguments);
    },
    /**
     * @override
     */
    start: function () {
        const _super = this._super.bind(this);
        return _super(...arguments);
    },
    /**
     * @override
     * @private
     */
    async _renderCustomXML(uiFragment) {
        await this._renderProductCategorySelector(uiFragment);
    },
    /**
     * Fetches product manual categories.
     * @private
     * @returns {Promise}
     */
    async _fetchProductManualCategories() {
        const res = await jsonrpc("/product_manual/categories");
        this.productManualCategories = res;
        return res;
    },
    /**
     * Renders the product manual categories option selector content into the provided uiFragment.
     * @private
     * @param {HTMLElement} uiFragment
     */
    async _renderProductCategorySelector(uiFragment) {
        const productManualCategories = await this._fetchProductManualCategories();
        const productCategoriesSelectorEl = uiFragment.querySelector(
            '[data-name="special_product_manual_snippet"]'
        );
        return this._renderSelectUserValueWidgetButtons(
            productCategoriesSelectorEl,
            productManualCategories
        );
    },
    /**
     * Renders we-buttons into a SelectUserValueWidget element according to provided data.
     * @private
     * @param {HTMLElement} selectUserValueWidgetElement The SelectUserValueWidget buttons
     * @param {Object} data
     */
    async _renderSelectUserValueWidgetButtons(selectUserValueWidgetElement, data) {
        for (let id in data) {
            const button = document.createElement("we-button");
            button.dataset.selectDataAttribute = id;
            if (data[id].thumb) {
                button.dataset.img = data[id].thumb;
            } else {
                button.innerText = data[id].name;
            }
            selectUserValueWidgetElement.appendChild(button);
        }
    },
    /**
     * Handler for selecting a category and rendering the products.
     * @param {string} previewMode
     * @param {Object} params
     */
    async selectItem(previewMode, params) {
        const category = this.productManualCategories[params.activeValue];
        if (category) {
            const categoryId = category.id;
            const products = await this._fetchProductsByCategory(categoryId);
            const temp = renderToFragment(
                "custom_vcs_Product_manual.second_dynamic_product_manual",
                {
                    ...products,
                }
            );
            const tempDiv = document.createElement("div");
            tempDiv.appendChild(temp);
            // add the product to the container
            this.$target.find(".product-manual-container").empty().append(tempDiv.innerHTML);
        }
    },
    /**
     * Fetches list product manual categories.
     * @private
     * @returns {Promise}
     */
    async _fetchProductsByCategory(categoryId) {
        try {
            const res = await jsonrpc("/product_manual/get_data", {
                method: "call",
                params: { category_id: categoryId },
            });
            return res;
        } catch (error) {
            console.error("Error fetching product manual:", error);
            return {};
        }
    },
});