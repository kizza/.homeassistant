/******************************************************************************
Copyright (c) Microsoft Corporation.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
***************************************************************************** */

function __decorate(decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
}

function __awaiter(thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
}

/**
 * @license
 * Copyright 2019 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */
const t$5=window,e$7=t$5.ShadowRoot&&(void 0===t$5.ShadyCSS||t$5.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,s$6=Symbol(),n$7=new WeakMap;class o$6{constructor(t,e,n){if(this._$cssResult$=!0,n!==s$6)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=t,this.t=e;}get styleSheet(){let t=this.o;const s=this.t;if(e$7&&void 0===t){const e=void 0!==s&&1===s.length;e&&(t=n$7.get(s)),void 0===t&&((this.o=t=new CSSStyleSheet).replaceSync(this.cssText),e&&n$7.set(s,t));}return t}toString(){return this.cssText}}const r$6=t=>new o$6("string"==typeof t?t:t+"",void 0,s$6),S$3=(s,n)=>{e$7?s.adoptedStyleSheets=n.map((t=>t instanceof CSSStyleSheet?t:t.styleSheet)):n.forEach((e=>{const n=document.createElement("style"),o=t$5.litNonce;void 0!==o&&n.setAttribute("nonce",o),n.textContent=e.cssText,s.appendChild(n);}));},c$3=e$7?t=>t:t=>t instanceof CSSStyleSheet?(t=>{let e="";for(const s of t.cssRules)e+=s.cssText;return r$6(e)})(t):t;

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */var s$5;const e$6=window,r$5=e$6.trustedTypes,h$3=r$5?r$5.emptyScript:"",o$5=e$6.reactiveElementPolyfillSupport,n$6={toAttribute(t,i){switch(i){case Boolean:t=t?h$3:null;break;case Object:case Array:t=null==t?t:JSON.stringify(t);}return t},fromAttribute(t,i){let s=t;switch(i){case Boolean:s=null!==t;break;case Number:s=null===t?null:Number(t);break;case Object:case Array:try{s=JSON.parse(t);}catch(t){s=null;}}return s}},a$3=(t,i)=>i!==t&&(i==i||t==t),l$4={attribute:!0,type:String,converter:n$6,reflect:!1,hasChanged:a$3};class d$3 extends HTMLElement{constructor(){super(),this._$Ei=new Map,this.isUpdatePending=!1,this.hasUpdated=!1,this._$El=null,this.u();}static addInitializer(t){var i;this.finalize(),(null!==(i=this.h)&&void 0!==i?i:this.h=[]).push(t);}static get observedAttributes(){this.finalize();const t=[];return this.elementProperties.forEach(((i,s)=>{const e=this._$Ep(s,i);void 0!==e&&(this._$Ev.set(e,s),t.push(e));})),t}static createProperty(t,i=l$4){if(i.state&&(i.attribute=!1),this.finalize(),this.elementProperties.set(t,i),!i.noAccessor&&!this.prototype.hasOwnProperty(t)){const s="symbol"==typeof t?Symbol():"__"+t,e=this.getPropertyDescriptor(t,s,i);void 0!==e&&Object.defineProperty(this.prototype,t,e);}}static getPropertyDescriptor(t,i,s){return {get(){return this[i]},set(e){const r=this[t];this[i]=e,this.requestUpdate(t,r,s);},configurable:!0,enumerable:!0}}static getPropertyOptions(t){return this.elementProperties.get(t)||l$4}static finalize(){if(this.hasOwnProperty("finalized"))return !1;this.finalized=!0;const t=Object.getPrototypeOf(this);if(t.finalize(),void 0!==t.h&&(this.h=[...t.h]),this.elementProperties=new Map(t.elementProperties),this._$Ev=new Map,this.hasOwnProperty("properties")){const t=this.properties,i=[...Object.getOwnPropertyNames(t),...Object.getOwnPropertySymbols(t)];for(const s of i)this.createProperty(s,t[s]);}return this.elementStyles=this.finalizeStyles(this.styles),!0}static finalizeStyles(i){const s=[];if(Array.isArray(i)){const e=new Set(i.flat(1/0).reverse());for(const i of e)s.unshift(c$3(i));}else void 0!==i&&s.push(c$3(i));return s}static _$Ep(t,i){const s=i.attribute;return !1===s?void 0:"string"==typeof s?s:"string"==typeof t?t.toLowerCase():void 0}u(){var t;this._$E_=new Promise((t=>this.enableUpdating=t)),this._$AL=new Map,this._$Eg(),this.requestUpdate(),null===(t=this.constructor.h)||void 0===t||t.forEach((t=>t(this)));}addController(t){var i,s;(null!==(i=this._$ES)&&void 0!==i?i:this._$ES=[]).push(t),void 0!==this.renderRoot&&this.isConnected&&(null===(s=t.hostConnected)||void 0===s||s.call(t));}removeController(t){var i;null===(i=this._$ES)||void 0===i||i.splice(this._$ES.indexOf(t)>>>0,1);}_$Eg(){this.constructor.elementProperties.forEach(((t,i)=>{this.hasOwnProperty(i)&&(this._$Ei.set(i,this[i]),delete this[i]);}));}createRenderRoot(){var t;const s=null!==(t=this.shadowRoot)&&void 0!==t?t:this.attachShadow(this.constructor.shadowRootOptions);return S$3(s,this.constructor.elementStyles),s}connectedCallback(){var t;void 0===this.renderRoot&&(this.renderRoot=this.createRenderRoot()),this.enableUpdating(!0),null===(t=this._$ES)||void 0===t||t.forEach((t=>{var i;return null===(i=t.hostConnected)||void 0===i?void 0:i.call(t)}));}enableUpdating(t){}disconnectedCallback(){var t;null===(t=this._$ES)||void 0===t||t.forEach((t=>{var i;return null===(i=t.hostDisconnected)||void 0===i?void 0:i.call(t)}));}attributeChangedCallback(t,i,s){this._$AK(t,s);}_$EO(t,i,s=l$4){var e;const r=this.constructor._$Ep(t,s);if(void 0!==r&&!0===s.reflect){const h=(void 0!==(null===(e=s.converter)||void 0===e?void 0:e.toAttribute)?s.converter:n$6).toAttribute(i,s.type);this._$El=t,null==h?this.removeAttribute(r):this.setAttribute(r,h),this._$El=null;}}_$AK(t,i){var s;const e=this.constructor,r=e._$Ev.get(t);if(void 0!==r&&this._$El!==r){const t=e.getPropertyOptions(r),h="function"==typeof t.converter?{fromAttribute:t.converter}:void 0!==(null===(s=t.converter)||void 0===s?void 0:s.fromAttribute)?t.converter:n$6;this._$El=r,this[r]=h.fromAttribute(i,t.type),this._$El=null;}}requestUpdate(t,i,s){let e=!0;void 0!==t&&(((s=s||this.constructor.getPropertyOptions(t)).hasChanged||a$3)(this[t],i)?(this._$AL.has(t)||this._$AL.set(t,i),!0===s.reflect&&this._$El!==t&&(void 0===this._$EC&&(this._$EC=new Map),this._$EC.set(t,s))):e=!1),!this.isUpdatePending&&e&&(this._$E_=this._$Ej());}async _$Ej(){this.isUpdatePending=!0;try{await this._$E_;}catch(t){Promise.reject(t);}const t=this.scheduleUpdate();return null!=t&&await t,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){var t;if(!this.isUpdatePending)return;this.hasUpdated,this._$Ei&&(this._$Ei.forEach(((t,i)=>this[i]=t)),this._$Ei=void 0);let i=!1;const s=this._$AL;try{i=this.shouldUpdate(s),i?(this.willUpdate(s),null===(t=this._$ES)||void 0===t||t.forEach((t=>{var i;return null===(i=t.hostUpdate)||void 0===i?void 0:i.call(t)})),this.update(s)):this._$Ek();}catch(t){throw i=!1,this._$Ek(),t}i&&this._$AE(s);}willUpdate(t){}_$AE(t){var i;null===(i=this._$ES)||void 0===i||i.forEach((t=>{var i;return null===(i=t.hostUpdated)||void 0===i?void 0:i.call(t)})),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(t)),this.updated(t);}_$Ek(){this._$AL=new Map,this.isUpdatePending=!1;}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$E_}shouldUpdate(t){return !0}update(t){void 0!==this._$EC&&(this._$EC.forEach(((t,i)=>this._$EO(i,this[i],t))),this._$EC=void 0),this._$Ek();}updated(t){}firstUpdated(t){}}d$3.finalized=!0,d$3.elementProperties=new Map,d$3.elementStyles=[],d$3.shadowRootOptions={mode:"open"},null==o$5||o$5({ReactiveElement:d$3}),(null!==(s$5=e$6.reactiveElementVersions)&&void 0!==s$5?s$5:e$6.reactiveElementVersions=[]).push("1.6.0");

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */
var t$4;const i$3=window,s$4=i$3.trustedTypes,e$5=s$4?s$4.createPolicy("lit-html",{createHTML:t=>t}):void 0,o$4=`lit$${(Math.random()+"").slice(9)}$`,n$5="?"+o$4,l$3=`<${n$5}>`,h$2=document,r$4=(t="")=>h$2.createComment(t),d$2=t=>null===t||"object"!=typeof t&&"function"!=typeof t,u$1=Array.isArray,c$2=t=>u$1(t)||"function"==typeof(null==t?void 0:t[Symbol.iterator]),v$1=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,a$2=/-->/g,f$1=/>/g,_$1=RegExp(">|[ \t\n\f\r](?:([^\\s\"'>=/]+)([ \t\n\f\r]*=[ \t\n\f\r]*(?:[^ \t\n\f\r\"'`<>=]|(\"|')|))|$)","g"),m$1=/'/g,p$1=/"/g,$$1=/^(?:script|style|textarea|title)$/i,x$1=Symbol.for("lit-noChange"),b$1=Symbol.for("lit-nothing"),T$1=new WeakMap,A$1=h$2.createTreeWalker(h$2,129,null,!1),E$1=(t,i)=>{const s=t.length-1,n=[];let h,r=2===i?"<svg>":"",d=v$1;for(let i=0;i<s;i++){const s=t[i];let e,u,c=-1,g=0;for(;g<s.length&&(d.lastIndex=g,u=d.exec(s),null!==u);)g=d.lastIndex,d===v$1?"!--"===u[1]?d=a$2:void 0!==u[1]?d=f$1:void 0!==u[2]?($$1.test(u[2])&&(h=RegExp("</"+u[2],"g")),d=_$1):void 0!==u[3]&&(d=_$1):d===_$1?">"===u[0]?(d=null!=h?h:v$1,c=-1):void 0===u[1]?c=-2:(c=d.lastIndex-u[2].length,e=u[1],d=void 0===u[3]?_$1:'"'===u[3]?p$1:m$1):d===p$1||d===m$1?d=_$1:d===a$2||d===f$1?d=v$1:(d=_$1,h=void 0);const y=d===_$1&&t[i+1].startsWith("/>")?" ":"";r+=d===v$1?s+l$3:c>=0?(n.push(e),s.slice(0,c)+"$lit$"+s.slice(c)+o$4+y):s+o$4+(-2===c?(n.push(void 0),i):y);}const u=r+(t[s]||"<?>")+(2===i?"</svg>":"");if(!Array.isArray(t)||!t.hasOwnProperty("raw"))throw Error("invalid template strings array");return [void 0!==e$5?e$5.createHTML(u):u,n]};class C$1{constructor({strings:t,_$litType$:i},e){let l;this.parts=[];let h=0,d=0;const u=t.length-1,c=this.parts,[v,a]=E$1(t,i);if(this.el=C$1.createElement(v,e),A$1.currentNode=this.el.content,2===i){const t=this.el.content,i=t.firstChild;i.remove(),t.append(...i.childNodes);}for(;null!==(l=A$1.nextNode())&&c.length<u;){if(1===l.nodeType){if(l.hasAttributes()){const t=[];for(const i of l.getAttributeNames())if(i.endsWith("$lit$")||i.startsWith(o$4)){const s=a[d++];if(t.push(i),void 0!==s){const t=l.getAttribute(s.toLowerCase()+"$lit$").split(o$4),i=/([.?@])?(.*)/.exec(s);c.push({type:1,index:h,name:i[2],strings:t,ctor:"."===i[1]?M$1:"?"===i[1]?k$1:"@"===i[1]?H$1:S$2});}else c.push({type:6,index:h});}for(const i of t)l.removeAttribute(i);}if($$1.test(l.tagName)){const t=l.textContent.split(o$4),i=t.length-1;if(i>0){l.textContent=s$4?s$4.emptyScript:"";for(let s=0;s<i;s++)l.append(t[s],r$4()),A$1.nextNode(),c.push({type:2,index:++h});l.append(t[i],r$4());}}}else if(8===l.nodeType)if(l.data===n$5)c.push({type:2,index:h});else {let t=-1;for(;-1!==(t=l.data.indexOf(o$4,t+1));)c.push({type:7,index:h}),t+=o$4.length-1;}h++;}}static createElement(t,i){const s=h$2.createElement("template");return s.innerHTML=t,s}}function P$1(t,i,s=t,e){var o,n,l,h;if(i===x$1)return i;let r=void 0!==e?null===(o=s._$Co)||void 0===o?void 0:o[e]:s._$Cl;const u=d$2(i)?void 0:i._$litDirective$;return (null==r?void 0:r.constructor)!==u&&(null===(n=null==r?void 0:r._$AO)||void 0===n||n.call(r,!1),void 0===u?r=void 0:(r=new u(t),r._$AT(t,s,e)),void 0!==e?(null!==(l=(h=s)._$Co)&&void 0!==l?l:h._$Co=[])[e]=r:s._$Cl=r),void 0!==r&&(i=P$1(t,r._$AS(t,i.values),r,e)),i}class V$1{constructor(t,i){this.u=[],this._$AN=void 0,this._$AD=t,this._$AM=i;}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}v(t){var i;const{el:{content:s},parts:e}=this._$AD,o=(null!==(i=null==t?void 0:t.creationScope)&&void 0!==i?i:h$2).importNode(s,!0);A$1.currentNode=o;let n=A$1.nextNode(),l=0,r=0,d=e[0];for(;void 0!==d;){if(l===d.index){let i;2===d.type?i=new N$1(n,n.nextSibling,this,t):1===d.type?i=new d.ctor(n,d.name,d.strings,this,t):6===d.type&&(i=new I$1(n,this,t)),this.u.push(i),d=e[++r];}l!==(null==d?void 0:d.index)&&(n=A$1.nextNode(),l++);}return o}p(t){let i=0;for(const s of this.u)void 0!==s&&(void 0!==s.strings?(s._$AI(t,s,i),i+=s.strings.length-2):s._$AI(t[i])),i++;}}class N$1{constructor(t,i,s,e){var o;this.type=2,this._$AH=b$1,this._$AN=void 0,this._$AA=t,this._$AB=i,this._$AM=s,this.options=e,this._$Cm=null===(o=null==e?void 0:e.isConnected)||void 0===o||o;}get _$AU(){var t,i;return null!==(i=null===(t=this._$AM)||void 0===t?void 0:t._$AU)&&void 0!==i?i:this._$Cm}get parentNode(){let t=this._$AA.parentNode;const i=this._$AM;return void 0!==i&&11===t.nodeType&&(t=i.parentNode),t}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(t,i=this){t=P$1(this,t,i),d$2(t)?t===b$1||null==t||""===t?(this._$AH!==b$1&&this._$AR(),this._$AH=b$1):t!==this._$AH&&t!==x$1&&this.g(t):void 0!==t._$litType$?this.$(t):void 0!==t.nodeType?this.T(t):c$2(t)?this.k(t):this.g(t);}O(t,i=this._$AB){return this._$AA.parentNode.insertBefore(t,i)}T(t){this._$AH!==t&&(this._$AR(),this._$AH=this.O(t));}g(t){this._$AH!==b$1&&d$2(this._$AH)?this._$AA.nextSibling.data=t:this.T(h$2.createTextNode(t)),this._$AH=t;}$(t){var i;const{values:s,_$litType$:e}=t,o="number"==typeof e?this._$AC(t):(void 0===e.el&&(e.el=C$1.createElement(e.h,this.options)),e);if((null===(i=this._$AH)||void 0===i?void 0:i._$AD)===o)this._$AH.p(s);else {const t=new V$1(o,this),i=t.v(this.options);t.p(s),this.T(i),this._$AH=t;}}_$AC(t){let i=T$1.get(t.strings);return void 0===i&&T$1.set(t.strings,i=new C$1(t)),i}k(t){u$1(this._$AH)||(this._$AH=[],this._$AR());const i=this._$AH;let s,e=0;for(const o of t)e===i.length?i.push(s=new N$1(this.O(r$4()),this.O(r$4()),this,this.options)):s=i[e],s._$AI(o),e++;e<i.length&&(this._$AR(s&&s._$AB.nextSibling,e),i.length=e);}_$AR(t=this._$AA.nextSibling,i){var s;for(null===(s=this._$AP)||void 0===s||s.call(this,!1,!0,i);t&&t!==this._$AB;){const i=t.nextSibling;t.remove(),t=i;}}setConnected(t){var i;void 0===this._$AM&&(this._$Cm=t,null===(i=this._$AP)||void 0===i||i.call(this,t));}}class S$2{constructor(t,i,s,e,o){this.type=1,this._$AH=b$1,this._$AN=void 0,this.element=t,this.name=i,this._$AM=e,this.options=o,s.length>2||""!==s[0]||""!==s[1]?(this._$AH=Array(s.length-1).fill(new String),this.strings=s):this._$AH=b$1;}get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}_$AI(t,i=this,s,e){const o=this.strings;let n=!1;if(void 0===o)t=P$1(this,t,i,0),n=!d$2(t)||t!==this._$AH&&t!==x$1,n&&(this._$AH=t);else {const e=t;let l,h;for(t=o[0],l=0;l<o.length-1;l++)h=P$1(this,e[s+l],i,l),h===x$1&&(h=this._$AH[l]),n||(n=!d$2(h)||h!==this._$AH[l]),h===b$1?t=b$1:t!==b$1&&(t+=(null!=h?h:"")+o[l+1]),this._$AH[l]=h;}n&&!e&&this.j(t);}j(t){t===b$1?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,null!=t?t:"");}}class M$1 extends S$2{constructor(){super(...arguments),this.type=3;}j(t){this.element[this.name]=t===b$1?void 0:t;}}const R$1=s$4?s$4.emptyScript:"";class k$1 extends S$2{constructor(){super(...arguments),this.type=4;}j(t){t&&t!==b$1?this.element.setAttribute(this.name,R$1):this.element.removeAttribute(this.name);}}class H$1 extends S$2{constructor(t,i,s,e,o){super(t,i,s,e,o),this.type=5;}_$AI(t,i=this){var s;if((t=null!==(s=P$1(this,t,i,0))&&void 0!==s?s:b$1)===x$1)return;const e=this._$AH,o=t===b$1&&e!==b$1||t.capture!==e.capture||t.once!==e.once||t.passive!==e.passive,n=t!==b$1&&(e===b$1||o);o&&this.element.removeEventListener(this.name,this,e),n&&this.element.addEventListener(this.name,this,t),this._$AH=t;}handleEvent(t){var i,s;"function"==typeof this._$AH?this._$AH.call(null!==(s=null===(i=this.options)||void 0===i?void 0:i.host)&&void 0!==s?s:this.element,t):this._$AH.handleEvent(t);}}class I$1{constructor(t,i,s){this.element=t,this.type=6,this._$AN=void 0,this._$AM=i,this.options=s;}get _$AU(){return this._$AM._$AU}_$AI(t){P$1(this,t);}}const z$1=i$3.litHtmlPolyfillSupport;null==z$1||z$1(C$1,N$1),(null!==(t$4=i$3.litHtmlVersions)&&void 0!==t$4?t$4:i$3.litHtmlVersions=[]).push("2.6.0");

/**
 * @license
 * Copyright 2019 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */
const t$3=window,e$4=t$3.ShadowRoot&&(void 0===t$3.ShadyCSS||t$3.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,s$3=Symbol(),n$4=new WeakMap;class o$3{constructor(t,e,n){if(this._$cssResult$=!0,n!==s$3)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=t,this.t=e;}get styleSheet(){let t=this.o;const s=this.t;if(e$4&&void 0===t){const e=void 0!==s&&1===s.length;e&&(t=n$4.get(s)),void 0===t&&((this.o=t=new CSSStyleSheet).replaceSync(this.cssText),e&&n$4.set(s,t));}return t}toString(){return this.cssText}}const r$3=t=>new o$3("string"==typeof t?t:t+"",void 0,s$3),i$2=(t,...e)=>{const n=1===t.length?t[0]:e.reduce(((e,s,n)=>e+(t=>{if(!0===t._$cssResult$)return t.cssText;if("number"==typeof t)return t;throw Error("Value passed to 'css' function must be a 'css' function result: "+t+". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.")})(s)+t[n+1]),t[0]);return new o$3(n,t,s$3)},S$1=(s,n)=>{e$4?s.adoptedStyleSheets=n.map((t=>t instanceof CSSStyleSheet?t:t.styleSheet)):n.forEach((e=>{const n=document.createElement("style"),o=t$3.litNonce;void 0!==o&&n.setAttribute("nonce",o),n.textContent=e.cssText,s.appendChild(n);}));},c$1=e$4?t=>t:t=>t instanceof CSSStyleSheet?(t=>{let e="";for(const s of t.cssRules)e+=s.cssText;return r$3(e)})(t):t;

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */var s$2;const e$3=window,r$2=e$3.trustedTypes,h$1=r$2?r$2.emptyScript:"",o$2=e$3.reactiveElementPolyfillSupport,n$3={toAttribute(t,i){switch(i){case Boolean:t=t?h$1:null;break;case Object:case Array:t=null==t?t:JSON.stringify(t);}return t},fromAttribute(t,i){let s=t;switch(i){case Boolean:s=null!==t;break;case Number:s=null===t?null:Number(t);break;case Object:case Array:try{s=JSON.parse(t);}catch(t){s=null;}}return s}},a$1=(t,i)=>i!==t&&(i==i||t==t),l$2={attribute:!0,type:String,converter:n$3,reflect:!1,hasChanged:a$1};class d$1 extends HTMLElement{constructor(){super(),this._$Ei=new Map,this.isUpdatePending=!1,this.hasUpdated=!1,this._$El=null,this.u();}static addInitializer(t){var i;this.finalize(),(null!==(i=this.h)&&void 0!==i?i:this.h=[]).push(t);}static get observedAttributes(){this.finalize();const t=[];return this.elementProperties.forEach(((i,s)=>{const e=this._$Ep(s,i);void 0!==e&&(this._$Ev.set(e,s),t.push(e));})),t}static createProperty(t,i=l$2){if(i.state&&(i.attribute=!1),this.finalize(),this.elementProperties.set(t,i),!i.noAccessor&&!this.prototype.hasOwnProperty(t)){const s="symbol"==typeof t?Symbol():"__"+t,e=this.getPropertyDescriptor(t,s,i);void 0!==e&&Object.defineProperty(this.prototype,t,e);}}static getPropertyDescriptor(t,i,s){return {get(){return this[i]},set(e){const r=this[t];this[i]=e,this.requestUpdate(t,r,s);},configurable:!0,enumerable:!0}}static getPropertyOptions(t){return this.elementProperties.get(t)||l$2}static finalize(){if(this.hasOwnProperty("finalized"))return !1;this.finalized=!0;const t=Object.getPrototypeOf(this);if(t.finalize(),void 0!==t.h&&(this.h=[...t.h]),this.elementProperties=new Map(t.elementProperties),this._$Ev=new Map,this.hasOwnProperty("properties")){const t=this.properties,i=[...Object.getOwnPropertyNames(t),...Object.getOwnPropertySymbols(t)];for(const s of i)this.createProperty(s,t[s]);}return this.elementStyles=this.finalizeStyles(this.styles),!0}static finalizeStyles(i){const s=[];if(Array.isArray(i)){const e=new Set(i.flat(1/0).reverse());for(const i of e)s.unshift(c$1(i));}else void 0!==i&&s.push(c$1(i));return s}static _$Ep(t,i){const s=i.attribute;return !1===s?void 0:"string"==typeof s?s:"string"==typeof t?t.toLowerCase():void 0}u(){var t;this._$E_=new Promise((t=>this.enableUpdating=t)),this._$AL=new Map,this._$Eg(),this.requestUpdate(),null===(t=this.constructor.h)||void 0===t||t.forEach((t=>t(this)));}addController(t){var i,s;(null!==(i=this._$ES)&&void 0!==i?i:this._$ES=[]).push(t),void 0!==this.renderRoot&&this.isConnected&&(null===(s=t.hostConnected)||void 0===s||s.call(t));}removeController(t){var i;null===(i=this._$ES)||void 0===i||i.splice(this._$ES.indexOf(t)>>>0,1);}_$Eg(){this.constructor.elementProperties.forEach(((t,i)=>{this.hasOwnProperty(i)&&(this._$Ei.set(i,this[i]),delete this[i]);}));}createRenderRoot(){var t;const s=null!==(t=this.shadowRoot)&&void 0!==t?t:this.attachShadow(this.constructor.shadowRootOptions);return S$1(s,this.constructor.elementStyles),s}connectedCallback(){var t;void 0===this.renderRoot&&(this.renderRoot=this.createRenderRoot()),this.enableUpdating(!0),null===(t=this._$ES)||void 0===t||t.forEach((t=>{var i;return null===(i=t.hostConnected)||void 0===i?void 0:i.call(t)}));}enableUpdating(t){}disconnectedCallback(){var t;null===(t=this._$ES)||void 0===t||t.forEach((t=>{var i;return null===(i=t.hostDisconnected)||void 0===i?void 0:i.call(t)}));}attributeChangedCallback(t,i,s){this._$AK(t,s);}_$EO(t,i,s=l$2){var e;const r=this.constructor._$Ep(t,s);if(void 0!==r&&!0===s.reflect){const h=(void 0!==(null===(e=s.converter)||void 0===e?void 0:e.toAttribute)?s.converter:n$3).toAttribute(i,s.type);this._$El=t,null==h?this.removeAttribute(r):this.setAttribute(r,h),this._$El=null;}}_$AK(t,i){var s;const e=this.constructor,r=e._$Ev.get(t);if(void 0!==r&&this._$El!==r){const t=e.getPropertyOptions(r),h="function"==typeof t.converter?{fromAttribute:t.converter}:void 0!==(null===(s=t.converter)||void 0===s?void 0:s.fromAttribute)?t.converter:n$3;this._$El=r,this[r]=h.fromAttribute(i,t.type),this._$El=null;}}requestUpdate(t,i,s){let e=!0;void 0!==t&&(((s=s||this.constructor.getPropertyOptions(t)).hasChanged||a$1)(this[t],i)?(this._$AL.has(t)||this._$AL.set(t,i),!0===s.reflect&&this._$El!==t&&(void 0===this._$EC&&(this._$EC=new Map),this._$EC.set(t,s))):e=!1),!this.isUpdatePending&&e&&(this._$E_=this._$Ej());}async _$Ej(){this.isUpdatePending=!0;try{await this._$E_;}catch(t){Promise.reject(t);}const t=this.scheduleUpdate();return null!=t&&await t,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){var t;if(!this.isUpdatePending)return;this.hasUpdated,this._$Ei&&(this._$Ei.forEach(((t,i)=>this[i]=t)),this._$Ei=void 0);let i=!1;const s=this._$AL;try{i=this.shouldUpdate(s),i?(this.willUpdate(s),null===(t=this._$ES)||void 0===t||t.forEach((t=>{var i;return null===(i=t.hostUpdate)||void 0===i?void 0:i.call(t)})),this.update(s)):this._$Ek();}catch(t){throw i=!1,this._$Ek(),t}i&&this._$AE(s);}willUpdate(t){}_$AE(t){var i;null===(i=this._$ES)||void 0===i||i.forEach((t=>{var i;return null===(i=t.hostUpdated)||void 0===i?void 0:i.call(t)})),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(t)),this.updated(t);}_$Ek(){this._$AL=new Map,this.isUpdatePending=!1;}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$E_}shouldUpdate(t){return !0}update(t){void 0!==this._$EC&&(this._$EC.forEach(((t,i)=>this._$EO(i,this[i],t))),this._$EC=void 0),this._$Ek();}updated(t){}firstUpdated(t){}}d$1.finalized=!0,d$1.elementProperties=new Map,d$1.elementStyles=[],d$1.shadowRootOptions={mode:"open"},null==o$2||o$2({ReactiveElement:d$1}),(null!==(s$2=e$3.reactiveElementVersions)&&void 0!==s$2?s$2:e$3.reactiveElementVersions=[]).push("1.5.0");

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */
var t$2;const i$1=window,s$1=i$1.trustedTypes,e$2=s$1?s$1.createPolicy("lit-html",{createHTML:t=>t}):void 0,o$1=`lit$${(Math.random()+"").slice(9)}$`,n$2="?"+o$1,l$1=`<${n$2}>`,h=document,r$1=(t="")=>h.createComment(t),d=t=>null===t||"object"!=typeof t&&"function"!=typeof t,u=Array.isArray,c=t=>u(t)||"function"==typeof(null==t?void 0:t[Symbol.iterator]),v=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,a=/-->/g,f=/>/g,_=RegExp(">|[ \t\n\f\r](?:([^\\s\"'>=/]+)([ \t\n\f\r]*=[ \t\n\f\r]*(?:[^ \t\n\f\r\"'`<>=]|(\"|')|))|$)","g"),m=/'/g,p=/"/g,$=/^(?:script|style|textarea|title)$/i,g=t=>(i,...s)=>({_$litType$:t,strings:i,values:s}),y=g(1),x=Symbol.for("lit-noChange"),b=Symbol.for("lit-nothing"),T=new WeakMap,A=h.createTreeWalker(h,129,null,!1),E=(t,i)=>{const s=t.length-1,n=[];let h,r=2===i?"<svg>":"",d=v;for(let i=0;i<s;i++){const s=t[i];let e,u,c=-1,g=0;for(;g<s.length&&(d.lastIndex=g,u=d.exec(s),null!==u);)g=d.lastIndex,d===v?"!--"===u[1]?d=a:void 0!==u[1]?d=f:void 0!==u[2]?($.test(u[2])&&(h=RegExp("</"+u[2],"g")),d=_):void 0!==u[3]&&(d=_):d===_?">"===u[0]?(d=null!=h?h:v,c=-1):void 0===u[1]?c=-2:(c=d.lastIndex-u[2].length,e=u[1],d=void 0===u[3]?_:'"'===u[3]?p:m):d===p||d===m?d=_:d===a||d===f?d=v:(d=_,h=void 0);const y=d===_&&t[i+1].startsWith("/>")?" ":"";r+=d===v?s+l$1:c>=0?(n.push(e),s.slice(0,c)+"$lit$"+s.slice(c)+o$1+y):s+o$1+(-2===c?(n.push(void 0),i):y);}const u=r+(t[s]||"<?>")+(2===i?"</svg>":"");if(!Array.isArray(t)||!t.hasOwnProperty("raw"))throw Error("invalid template strings array");return [void 0!==e$2?e$2.createHTML(u):u,n]};class C{constructor({strings:t,_$litType$:i},e){let l;this.parts=[];let h=0,d=0;const u=t.length-1,c=this.parts,[v,a]=E(t,i);if(this.el=C.createElement(v,e),A.currentNode=this.el.content,2===i){const t=this.el.content,i=t.firstChild;i.remove(),t.append(...i.childNodes);}for(;null!==(l=A.nextNode())&&c.length<u;){if(1===l.nodeType){if(l.hasAttributes()){const t=[];for(const i of l.getAttributeNames())if(i.endsWith("$lit$")||i.startsWith(o$1)){const s=a[d++];if(t.push(i),void 0!==s){const t=l.getAttribute(s.toLowerCase()+"$lit$").split(o$1),i=/([.?@])?(.*)/.exec(s);c.push({type:1,index:h,name:i[2],strings:t,ctor:"."===i[1]?M:"?"===i[1]?k:"@"===i[1]?H:S});}else c.push({type:6,index:h});}for(const i of t)l.removeAttribute(i);}if($.test(l.tagName)){const t=l.textContent.split(o$1),i=t.length-1;if(i>0){l.textContent=s$1?s$1.emptyScript:"";for(let s=0;s<i;s++)l.append(t[s],r$1()),A.nextNode(),c.push({type:2,index:++h});l.append(t[i],r$1());}}}else if(8===l.nodeType)if(l.data===n$2)c.push({type:2,index:h});else {let t=-1;for(;-1!==(t=l.data.indexOf(o$1,t+1));)c.push({type:7,index:h}),t+=o$1.length-1;}h++;}}static createElement(t,i){const s=h.createElement("template");return s.innerHTML=t,s}}function P(t,i,s=t,e){var o,n,l,h;if(i===x)return i;let r=void 0!==e?null===(o=s._$Co)||void 0===o?void 0:o[e]:s._$Cl;const u=d(i)?void 0:i._$litDirective$;return (null==r?void 0:r.constructor)!==u&&(null===(n=null==r?void 0:r._$AO)||void 0===n||n.call(r,!1),void 0===u?r=void 0:(r=new u(t),r._$AT(t,s,e)),void 0!==e?(null!==(l=(h=s)._$Co)&&void 0!==l?l:h._$Co=[])[e]=r:s._$Cl=r),void 0!==r&&(i=P(t,r._$AS(t,i.values),r,e)),i}class V{constructor(t,i){this.u=[],this._$AN=void 0,this._$AD=t,this._$AM=i;}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}v(t){var i;const{el:{content:s},parts:e}=this._$AD,o=(null!==(i=null==t?void 0:t.creationScope)&&void 0!==i?i:h).importNode(s,!0);A.currentNode=o;let n=A.nextNode(),l=0,r=0,d=e[0];for(;void 0!==d;){if(l===d.index){let i;2===d.type?i=new N(n,n.nextSibling,this,t):1===d.type?i=new d.ctor(n,d.name,d.strings,this,t):6===d.type&&(i=new I(n,this,t)),this.u.push(i),d=e[++r];}l!==(null==d?void 0:d.index)&&(n=A.nextNode(),l++);}return o}p(t){let i=0;for(const s of this.u)void 0!==s&&(void 0!==s.strings?(s._$AI(t,s,i),i+=s.strings.length-2):s._$AI(t[i])),i++;}}class N{constructor(t,i,s,e){var o;this.type=2,this._$AH=b,this._$AN=void 0,this._$AA=t,this._$AB=i,this._$AM=s,this.options=e,this._$Cm=null===(o=null==e?void 0:e.isConnected)||void 0===o||o;}get _$AU(){var t,i;return null!==(i=null===(t=this._$AM)||void 0===t?void 0:t._$AU)&&void 0!==i?i:this._$Cm}get parentNode(){let t=this._$AA.parentNode;const i=this._$AM;return void 0!==i&&11===t.nodeType&&(t=i.parentNode),t}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(t,i=this){t=P(this,t,i),d(t)?t===b||null==t||""===t?(this._$AH!==b&&this._$AR(),this._$AH=b):t!==this._$AH&&t!==x&&this.g(t):void 0!==t._$litType$?this.$(t):void 0!==t.nodeType?this.T(t):c(t)?this.k(t):this.g(t);}O(t,i=this._$AB){return this._$AA.parentNode.insertBefore(t,i)}T(t){this._$AH!==t&&(this._$AR(),this._$AH=this.O(t));}g(t){this._$AH!==b&&d(this._$AH)?this._$AA.nextSibling.data=t:this.T(h.createTextNode(t)),this._$AH=t;}$(t){var i;const{values:s,_$litType$:e}=t,o="number"==typeof e?this._$AC(t):(void 0===e.el&&(e.el=C.createElement(e.h,this.options)),e);if((null===(i=this._$AH)||void 0===i?void 0:i._$AD)===o)this._$AH.p(s);else {const t=new V(o,this),i=t.v(this.options);t.p(s),this.T(i),this._$AH=t;}}_$AC(t){let i=T.get(t.strings);return void 0===i&&T.set(t.strings,i=new C(t)),i}k(t){u(this._$AH)||(this._$AH=[],this._$AR());const i=this._$AH;let s,e=0;for(const o of t)e===i.length?i.push(s=new N(this.O(r$1()),this.O(r$1()),this,this.options)):s=i[e],s._$AI(o),e++;e<i.length&&(this._$AR(s&&s._$AB.nextSibling,e),i.length=e);}_$AR(t=this._$AA.nextSibling,i){var s;for(null===(s=this._$AP)||void 0===s||s.call(this,!1,!0,i);t&&t!==this._$AB;){const i=t.nextSibling;t.remove(),t=i;}}setConnected(t){var i;void 0===this._$AM&&(this._$Cm=t,null===(i=this._$AP)||void 0===i||i.call(this,t));}}class S{constructor(t,i,s,e,o){this.type=1,this._$AH=b,this._$AN=void 0,this.element=t,this.name=i,this._$AM=e,this.options=o,s.length>2||""!==s[0]||""!==s[1]?(this._$AH=Array(s.length-1).fill(new String),this.strings=s):this._$AH=b;}get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}_$AI(t,i=this,s,e){const o=this.strings;let n=!1;if(void 0===o)t=P(this,t,i,0),n=!d(t)||t!==this._$AH&&t!==x,n&&(this._$AH=t);else {const e=t;let l,h;for(t=o[0],l=0;l<o.length-1;l++)h=P(this,e[s+l],i,l),h===x&&(h=this._$AH[l]),n||(n=!d(h)||h!==this._$AH[l]),h===b?t=b:t!==b&&(t+=(null!=h?h:"")+o[l+1]),this._$AH[l]=h;}n&&!e&&this.j(t);}j(t){t===b?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,null!=t?t:"");}}class M extends S{constructor(){super(...arguments),this.type=3;}j(t){this.element[this.name]=t===b?void 0:t;}}const R=s$1?s$1.emptyScript:"";class k extends S{constructor(){super(...arguments),this.type=4;}j(t){t&&t!==b?this.element.setAttribute(this.name,R):this.element.removeAttribute(this.name);}}class H extends S{constructor(t,i,s,e,o){super(t,i,s,e,o),this.type=5;}_$AI(t,i=this){var s;if((t=null!==(s=P(this,t,i,0))&&void 0!==s?s:b)===x)return;const e=this._$AH,o=t===b&&e!==b||t.capture!==e.capture||t.once!==e.once||t.passive!==e.passive,n=t!==b&&(e===b||o);o&&this.element.removeEventListener(this.name,this,e),n&&this.element.addEventListener(this.name,this,t),this._$AH=t;}handleEvent(t){var i,s;"function"==typeof this._$AH?this._$AH.call(null!==(s=null===(i=this.options)||void 0===i?void 0:i.host)&&void 0!==s?s:this.element,t):this._$AH.handleEvent(t);}}class I{constructor(t,i,s){this.element=t,this.type=6,this._$AN=void 0,this._$AM=i,this.options=s;}get _$AU(){return this._$AM._$AU}_$AI(t){P(this,t);}}const z=i$1.litHtmlPolyfillSupport;null==z||z(C,N),(null!==(t$2=i$1.litHtmlVersions)&&void 0!==t$2?t$2:i$1.litHtmlVersions=[]).push("2.5.0");const Z=(t,i,s)=>{var e,o;const n=null!==(e=null==s?void 0:s.renderBefore)&&void 0!==e?e:i;let l=n._$litPart$;if(void 0===l){const t=null!==(o=null==s?void 0:s.renderBefore)&&void 0!==o?o:null;n._$litPart$=l=new N(i.insertBefore(r$1(),t),t,void 0,null!=s?s:{});}return l._$AI(t),l};

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */var l,o;class s extends d$1{constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0;}createRenderRoot(){var t,e;const i=super.createRenderRoot();return null!==(t=(e=this.renderOptions).renderBefore)&&void 0!==t||(e.renderBefore=i.firstChild),i}update(t){const i=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(t),this._$Do=Z(i,this.renderRoot,this.renderOptions);}connectedCallback(){var t;super.connectedCallback(),null===(t=this._$Do)||void 0===t||t.setConnected(!0);}disconnectedCallback(){var t;super.disconnectedCallback(),null===(t=this._$Do)||void 0===t||t.setConnected(!1);}render(){return x}}s.finalized=!0,s._$litElement$=!0,null===(l=globalThis.litElementHydrateSupport)||void 0===l||l.call(globalThis,{LitElement:s});const n$1=globalThis.litElementPolyfillSupport;null==n$1||n$1({LitElement:s});(null!==(o=globalThis.litElementVersions)&&void 0!==o?o:globalThis.litElementVersions=[]).push("3.2.2");

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */
const e$1=e=>n=>"function"==typeof n?((e,n)=>(customElements.define(e,n),n))(e,n):((e,n)=>{const{kind:t,elements:s}=n;return {kind:t,elements:s,finisher(n){customElements.define(e,n);}}})(e,n);

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */
const i=(i,e)=>"method"===e.kind&&e.descriptor&&!("value"in e.descriptor)?{...e,finisher(n){n.createProperty(e.key,i);}}:{kind:"field",key:Symbol(),placement:"own",descriptor:{},originalKey:e.key,initializer(){"function"==typeof e.initializer&&(this[e.key]=e.initializer.call(this));},finisher(n){n.createProperty(e.key,i);}};function e(e){return (n,t)=>void 0!==t?((i,e,n)=>{e.constructor.createProperty(n,i);})(e,n,t):i(e,n)}

/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */function t$1(t){return e({...t,state:!0})}

/**
 * @license
 * Copyright 2021 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */var n;null!=(null===(n=window.HTMLSlotElement)||void 0===n?void 0:n.prototype.assignedElements)?(o,n)=>o.assignedElements(n):(o,n)=>o.assignedNodes(n).filter((o=>o.nodeType===Node.ELEMENT_NODE));

const CARD_VERSION = '0.0.1';
const RADIUS = i$2 `0.8em`;
const colours = {
    maroon: [128, 0, 0],
    'dark red': [139, 0, 0],
    brown: [165, 42, 42],
    firebrick: [178, 34, 34],
    crimson: [220, 20, 60],
    red: [255, 0, 0],
    tomato: [255, 99, 71],
    coral: [255, 127, 80],
    'indian red': [205, 92, 92],
    'light coral': [240, 128, 128],
    'dark salmon': [233, 150, 122],
    salmon: [250, 128, 114],
    'light salmon': [255, 160, 122],
    'orange red': [255, 69, 0],
    'dark orange': [255, 140, 0],
    orange: [255, 165, 0],
    gold: [255, 215, 0],
    'dark golden rod': [184, 134, 11],
    'golden rod': [218, 165, 32],
    'pale golden rod': [238, 232, 170],
    'dark khaki': [189, 183, 107],
    khaki: [240, 230, 140],
    olive: [128, 128, 0],
    yellow: [255, 255, 0],
    'yellow green': [154, 205, 50],
    'dark olive green': [85, 107, 47],
    'olive drab': [107, 142, 35],
    'lawn green': [124, 252, 0],
    chartreuse: [127, 255, 0],
    'green yellow': [173, 255, 47],
    'dark green': [0, 100, 0],
    green: [0, 128, 0],
    'forest green': [34, 139, 34],
    lime: [0, 255, 0],
    'lime green': [50, 205, 50],
    'light green': [144, 238, 144],
    'pale green': [152, 251, 152],
    'dark sea green': [143, 188, 143],
    'medium spring green': [0, 250, 154],
    'spring green': [0, 255, 127],
    'sea green': [46, 139, 87],
    'medium aqua marine': [102, 205, 170],
    'medium sea green': [60, 179, 113],
    'light sea green': [32, 178, 170],
    'dark slate gray': [47, 79, 79],
    teal: [0, 128, 128],
    'dark cyan': [0, 139, 139],
    aqua: [0, 255, 255],
    cyan: [0, 255, 255],
    'light cyan': [224, 255, 255],
    'dark turquoise': [0, 206, 209],
    turquoise: [64, 224, 208],
    'medium turquoise': [72, 209, 204],
    'pale turquoise': [175, 238, 238],
    'aqua marine': [127, 255, 212],
    'powder blue': [176, 224, 230],
    'cadet blue': [95, 158, 160],
    'steel blue': [70, 130, 180],
    'corn flower blue': [100, 149, 237],
    'deep sky blue': [0, 191, 255],
    'dodger blue': [30, 144, 255],
    'light blue': [173, 216, 230],
    'sky blue': [135, 206, 235],
    'light sky blue': [135, 206, 250],
    'midnight blue': [25, 25, 112],
    navy: [0, 0, 128],
    'dark blue': [0, 0, 139],
    'medium blue': [0, 0, 205],
    blue: [0, 0, 255],
    'royal blue': [65, 105, 225],
    'blue violet': [138, 43, 226],
    indigo: [75, 0, 130],
    'dark slate blue': [72, 61, 139],
    'slate blue': [106, 90, 205],
    'medium slate blue': [123, 104, 238],
    'medium purple': [147, 112, 219],
    'dark magenta': [139, 0, 139],
    'dark violet': [148, 0, 211],
    'dark orchid': [153, 50, 204],
    'medium orchid': [186, 85, 211],
    purple: [128, 0, 128],
    thistle: [216, 191, 216],
    plum: [221, 160, 221],
    violet: [238, 130, 238],
    'magenta / fuchsia': [255, 0, 255],
    orchid: [218, 112, 214],
    'medium violet red': [199, 21, 133],
    'pale violet red': [219, 112, 147],
    'deep pink': [255, 20, 147],
    'hot pink': [255, 105, 180],
    'light pink': [255, 182, 193],
    pink: [255, 192, 203],
    'antique white': [250, 235, 215],
    beige: [245, 245, 220],
    bisque: [255, 228, 196],
    'blanched almond': [255, 235, 205],
    wheat: [245, 222, 179],
    'corn silk': [255, 248, 220],
    'lemon chiffon': [255, 250, 205],
    'light golden rod yellow': [250, 250, 210],
    'light yellow': [255, 255, 224],
    'saddle brown': [139, 69, 19],
    sienna: [160, 82, 45],
    chocolate: [210, 105, 30],
    peru: [205, 133, 63],
    'sandy brown': [244, 164, 96],
    'burly wood': [222, 184, 135],
    tan: [210, 180, 140],
    'rosy brown': [188, 143, 143],
    moccasin: [255, 228, 181],
    'navajo white': [255, 222, 173],
    'peach puff': [255, 218, 185],
    'misty rose': [255, 228, 225],
    'lavender blush': [255, 240, 245],
    linen: [250, 240, 230],
    'old lace': [253, 245, 230],
    'papaya whip': [255, 239, 213],
    'sea shell': [255, 245, 238],
    'mint cream': [245, 255, 250],
    'slate gray': [112, 128, 144],
    'light slate gray': [119, 136, 153],
    'light steel blue': [176, 196, 222],
    lavender: [230, 230, 250],
    'floral white': [255, 250, 240],
    'alice blue': [240, 248, 255],
    'ghost white': [248, 248, 255],
    honeydew: [240, 255, 240],
    ivory: [255, 255, 240],
    azure: [240, 255, 255],
    snow: [255, 250, 250],
    black: [0, 0, 0],
    'dim gray / dim grey': [105, 105, 105],
    'gray / grey': [128, 128, 128],
    'dark gray / dark grey': [169, 169, 169],
    silver: [192, 192, 192],
    'light gray / light grey': [211, 211, 211],
    gainsboro: [220, 220, 220],
    'white smoke': [245, 245, 245],
    white: [255, 255, 255],
};

const loadHomeAsssistantComponents = () => {
    var _a;
    if (!customElements.get('ha-entity-picker')) {
        (_a = customElements.get('hui-entities-card')) === null || _a === void 0 ? void 0 : _a.getConfigElement();
    }
};
const colourName = (colour) => Object.keys(colours).find(colourName => JSON.stringify(colours[colourName]) === JSON.stringify(colour)) || colour.join('');
const linearGradient = (colours) => colours.length === 1
    ? `rgb(${colours[0].join(', ')})`
    : `linear-gradient(to right, ${colours.map(rgb => `rgb(${rgb.join(', ')})`).join(', ')})`;
const labelColour = (background) => {
    const [red, green, blue] = background;
    const yiq = (red * 299 + green * 587 + blue * 114) / 1000;
    if (yiq < 128) {
        return i$2 `rgba(255, 255, 255, 0.8)`;
    }
    else {
        return i$2 `rgba(10, 10, 10, 0.6)`;
    }
};
const DOUBLE_CLICK_TIMEOUT = 250;
const withDoubleClick = (handler) => (e) => {
    const interval = DOUBLE_CLICK_TIMEOUT;
    const state = document;
    clearTimeout(state.clickedTimer);
    // Check if it's a double click
    if (state.clicked && state.clicked.key == e.target) {
        const delta = Date.now() - state.clicked.timestamp;
        if (delta < interval) {
            return handler(true);
        }
    }
    // Store for double click
    state.clicked = { key: e.target, timestamp: Date.now() };
    state.clickedTimer = setTimeout(() => {
        state.clicked = undefined;
        handler(false);
    }, interval);
};

let Chip = class Chip extends s {
    constructor() {
        super();
        this.colour = [255, 0, 0];
        this.index = -1;
        this.render = () => y `<span style="color: ${labelColour(this.colour)}"> ${colourName(this.colour)} </span>`;
        this.clickHandler = withDoubleClick((doubleClicked) => this.dispatchEvent(new CustomEvent(doubleClicked ? 'doubleClick' : 'singleClick', {
            detail: {
                colour: this.colour,
                index: this.index,
            },
            bubbles: true,
            composed: true,
        })));
        this.addEventListener('click', this.clickHandler);
    }
    shouldUpdate(changedProperties) {
        return changedProperties.has('colour');
    }
    updated() {
        this.style.background = `rgb(${this.colour})`;
    }
};
Chip.styles = i$2 `
    :host {
      border-radius: ${RADIUS};
      cursor: default;
      display: inline-block;
      padding: 0.5em 1em;
      white-space: nowrap;
    }
    :host(:active) {
      text-decoration: underline;
    }
  `;
__decorate([
    e({ attribute: false })
], Chip.prototype, "hass", void 0);
__decorate([
    e({ attribute: false })
], Chip.prototype, "colour", void 0);
__decorate([
    e({ attribute: false })
], Chip.prototype, "index", void 0);
Chip = __decorate([
    e$1('magic-home-party-chip')
], Chip);

let Palette = class Palette extends s {
    constructor() {
        super(...arguments);
        this.colours = [];
        this.render = () => {
            if (this.colours.length === 0) {
                return y `No colours`;
            }
            return y `
      <div class="palette">
        ${this.colours.map((colour, index) => y `
            <magic-home-party-chip
              .hass="${this.hass}"
              .colour="${colour}"
              .index="${index}"
            />
          `)}
      </div>
    `;
        };
    }
};
Palette.styles = i$2 `
    :host {
    }

    .palette {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5em;
      max-height: 34vh;
      overflow-y: scroll;
      row-gap: 0.5em;
    }
  `;
__decorate([
    e({ attribute: false })
], Palette.prototype, "hass", void 0);
__decorate([
    e({ attribute: false })
], Palette.prototype, "colours", void 0);
Palette = __decorate([
    e$1('magic-home-party-palette')
], Palette);

console.info(`%c  MAGIC-HOME-PARTY-CARD \n%c  Version ${CARD_VERSION}    `, 'color: white; font-weight: bold; background: purple', 'color: white; font-weight: bold; background: dimgray');
// Register to UI picker
window.customCards = window.customCards || [];
window.customCards.push({
    type: 'magic-home-party-card',
    name: 'Magic Home Party Card',
    description: 'Have a party with your magic home lights',
});
let MagicHomeParty = class MagicHomeParty extends s {
    constructor() {
        super(...arguments);
        this.playEffect = () => this.hass.callService('flux_led', 'set_custom_effect', {
            entity_id: this.config.entities,
            colors: this.config.colours,
            transition: 'gradual',
        });
    }
    setConfig(config) {
        this.config = Object.assign(Object.assign({}, config), { title: '', entities: config.entities || [] });
    }
    render() {
        if (!this.hass || !this.config) {
            return y ``;
        }
        if (this.config.colours.length === 0) {
            return y `No colours selected`;
        }
        const foreground = labelColour(this.config.colours[0]);
        const entitiesHtml = this.stateEntities.map(stateEntity => y `<div class="entity">
          <state-badge .stateObj=${stateEntity} style="color: ${foreground};"></state-badge>
          ${stateEntity.attributes.friendly_name || stateEntity.entity_id}
        </div>`);
        return y `
      <ha-card @click=${this.playEffect}>
        <div
          class="gradient"
          style="color: ${foreground}; background: ${linearGradient(this.config.colours)}"
        >
          <div class="entities">${entitiesHtml}</div>
        </div>
      </ha-card>
    `;
    }
    static getConfigElement() {
        return __awaiter(this, void 0, void 0, function* () {
            yield Promise.resolve().then(function () { return editor; });
            return document.createElement('magic-home-party-card-editor');
        });
    }
    static getStubConfig() {
        return { entities: [] };
    }
    get stateEntities() {
        return this.config.entities.map(entity => this.hass.states[entity]);
    }
};
MagicHomeParty.styles = i$2 `
    .gradient {
      padding-top: 3em;
      border-radius: var(--ha-card-border-radius, 12px);
      display: flex;
      align-items: end;
      color: #fff;
    }

    .entities {
      padding: 1em 0.5em;
      display: flex;
      flex-wrap: wrap;
    }

    .entity {
      display: flex;
      align-items: center;
      border-radius: ${RADIUS};
      max-height: 1.6em;
    }
  `;
__decorate([
    e({ attribute: false })
], MagicHomeParty.prototype, "hass", void 0);
__decorate([
    t$1()
], MagicHomeParty.prototype, "config", void 0);
MagicHomeParty = __decorate([
    e$1('magic-home-party-card')
], MagicHomeParty);

var __assign$1 = (window && window.__assign) || function () {
    __assign$1 = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign$1.apply(this, arguments);
};

// https://tc39.es/ecma402/#sec-issanctionedsimpleunitidentifier
var SANCTIONED_UNITS = [
    'angle-degree',
    'area-acre',
    'area-hectare',
    'concentr-percent',
    'digital-bit',
    'digital-byte',
    'digital-gigabit',
    'digital-gigabyte',
    'digital-kilobit',
    'digital-kilobyte',
    'digital-megabit',
    'digital-megabyte',
    'digital-petabyte',
    'digital-terabit',
    'digital-terabyte',
    'duration-day',
    'duration-hour',
    'duration-millisecond',
    'duration-minute',
    'duration-month',
    'duration-second',
    'duration-week',
    'duration-year',
    'length-centimeter',
    'length-foot',
    'length-inch',
    'length-kilometer',
    'length-meter',
    'length-mile-scandinavian',
    'length-mile',
    'length-millimeter',
    'length-yard',
    'mass-gram',
    'mass-kilogram',
    'mass-ounce',
    'mass-pound',
    'mass-stone',
    'temperature-celsius',
    'temperature-fahrenheit',
    'volume-fluid-ounce',
    'volume-gallon',
    'volume-liter',
    'volume-milliliter',
];

SANCTIONED_UNITS.map(function (unit) {
    return unit.replace(/^(.*?)-/, '');
});

var __extends = (window && window.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __assign = (window && window.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
/** @class */ ((function (_super) {
    __extends(MissingLocaleDataError, _super);
    function MissingLocaleDataError() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.type = 'MISSING_LOCALE_DATA';
        return _this;
    }
    return MissingLocaleDataError;
})(Error));

var t,r;!function(e){e.language="language",e.system="system",e.comma_decimal="comma_decimal",e.decimal_comma="decimal_comma",e.space_comma="space_comma",e.none="none";}(t||(t={})),function(e){e.language="language",e.system="system",e.am_pm="12",e.twenty_four="24";}(r||(r={}));var ne=function(e,t,r,n){n=n||{},r=null==r?{}:r;var i=new Event(t,{bubbles:void 0===n.bubbles||n.bubbles,cancelable:Boolean(n.cancelable),composed:void 0===n.composed||n.composed});return i.detail=r,e.dispatchEvent(i),i};

let EntitiesPicker = class EntitiesPicker extends s {
    constructor() {
        super(...arguments);
        this.domains = ['light'];
        // The entity-picker states dropdown is cached
        // (breaking this with a different entity filter each tile
        this._buildEntityFilter = () => (e) => !this.value || !this.value.includes(e.entity_id);
        this.entityFilter = this._buildEntityFilter();
        this.render = () => y ` ${this.currentEntities.map(entityId => y `<ha-entity-picker
          allow-custom-entity
          .curValue=${entityId}
          .hass=${this.hass}
          .entityFilter=${this.entityFilter}
          .includeDomains=${this.domains}
          .value=${entityId}
          @value-changed=${this._entityChanged}
        ></ha-entity-picker>`)}
    <ha-entity-picker
      allow-custom-entity
      .hass=${this.hass}
      .entityFilter=${this.entityFilter}
      .includeDomains=${this.domains}
      .required=${!this.currentEntities.length}
      @value-changed=${this._addEntity}
    ></ha-entity-picker>`;
    }
    get currentEntities() {
        return this.value || [];
    }
    connectedCallback() {
        super.connectedCallback();
        void loadHomeAsssistantComponents();
    }
    _entityChanged(event) {
        event.stopPropagation();
        const currentValue = event.currentTarget.curValue;
        const newValue = event.detail.value;
        if (!newValue || this.currentEntities.includes(newValue)) {
            this._updateEntities(this.currentEntities.filter(entity => entity !== currentValue));
        }
        else {
            this._updateEntities(this.currentEntities.map(entity => (entity === currentValue ? newValue : entity)));
        }
    }
    _updateEntities(entities) {
        this.value = entities.filter(Boolean);
        ne(this, 'value-changed', { value: this.value });
        this.entityFilter = this._buildEntityFilter();
    }
    _addEntity(event) {
        event.stopPropagation();
        event.currentTarget.value = ''; // Reset value of adding element
        this._updateEntities([...this.currentEntities, event.detail.value]);
    }
};
__decorate([
    e({ attribute: false })
], EntitiesPicker.prototype, "hass", void 0);
__decorate([
    e({ type: Array })
], EntitiesPicker.prototype, "value", void 0);
__decorate([
    e()
], EntitiesPicker.prototype, "domains", void 0);
__decorate([
    t$1()
], EntitiesPicker.prototype, "entityFilter", void 0);
EntitiesPicker = __decorate([
    e$1('magic-home-party-entities-picker')
], EntitiesPicker);

const { values } = Object;
let MagicHomePartyEditor = class MagicHomePartyEditor extends s {
    constructor() {
        super(...arguments);
        this.selectedColours = [];
        this.selectedEntities = [];
        this._setLight = (colour) => this.hass.callService('light', 'turn_on', {
            entity_id: this.selectedEntities,
            rgb_color: colour,
        });
        this._addChip = (colour) => {
            this.selectedColours = [...this.selectedColours, colour];
            this._updateConfig();
        };
        this._removeChip = (index) => {
            this.selectedColours = [...this.selectedColours.filter((_, i) => i !== index)];
            this._updateConfig();
        };
    }
    setConfig(config) {
        this.config = Object.assign(Object.assign({}, config), { colours: config.colours || [], entities: config.entities || [] });
        this.selectedColours = this.config.colours;
        this.selectedEntities = this.config.entities;
    }
    render() {
        if (!this.hass || !this.config) {
            return y `No config`;
        }
        return y `
      <div style="display: flex; align-items: center;">
        <h3>Selected Colours</h3>
        <span class="copyButton" @click=${this._copyToClipboard}> Copy to clipboard </span>
      </div>
      <magic-home-party-palette
        id="selected"
        title="Selected"
        .colours="${this.selectedColours}"
        @singleClick="${(e) => this._setLight(e.detail.colour)}"
        @doubleClick="${(e) => this._removeChip(e.detail.index)}"
      ></magic-home-party-palette>

      <h3>Palette</h3>
      <magic-home-party-palette
        title="Palette"
        .colours="${values(colours)}"
        @singleClick="${(e) => this._setLight(e.detail.colour)}"
        @doubleClick="${(e) => this._addChip(e.detail.colour)}"
      ></magic-home-party-palette>

      <h3>Selected Lights</h3>
      <magic-home-party-entities-picker
        .
        .hass=${this.hass}
        .value=${this.config.entities}
        @value-changed=${this._entitiesChanged}
      >
      </magic-home-party-entities-picker>
    `;
    }
    _copyToClipboard() {
        const colours = this.selectedColours.map(colour => `  - [${colour.join(', ')}]`);
        navigator.clipboard.writeText(colours.join('\n'));
    }
    _entitiesChanged(event) {
        event.stopPropagation();
        this.selectedEntities = [...event.detail.value];
        this._updateConfig();
    }
    _updateConfig() {
        const newConfig = Object.assign(Object.assign({}, this.config), { colours: this.selectedColours, entities: this.selectedEntities });
        this.config = newConfig;
        ne(this, 'config-changed', { config: newConfig });
    }
};
MagicHomePartyEditor.styles = i$2 `
    :host {
      display: flex;
      flex-direction: column;
    }

    * + h3 {
      margin-top: 2em;
    }

    .copyButton {
      position: relative;
      top: 1px;
      margin-left: auto;
      color: var(--mdc-theme-primary, #6200ee);
      cursor: default;
      -webkit-font-smoothing: antialiased;
      font-family: var(
        --mdc-typography-button-font-family,
        var(--mdc-typography-font-family, Roboto, sans-serif)
      );
      font-size: var(--mdc-typography-button-font-size, 0.875rem);
      font-weight: var(--mdc-typography-button-font-weight, 500);
      letter-spacing: var(--mdc-typography-button-letter-spacing, 0.0892857em);
    }
  `;
__decorate([
    e({ attribute: false })
], MagicHomePartyEditor.prototype, "hass", void 0);
__decorate([
    t$1()
], MagicHomePartyEditor.prototype, "config", void 0);
__decorate([
    t$1()
], MagicHomePartyEditor.prototype, "selectedColours", void 0);
__decorate([
    t$1()
], MagicHomePartyEditor.prototype, "selectedEntities", void 0);
MagicHomePartyEditor = __decorate([
    e$1('magic-home-party-card-editor')
], MagicHomePartyEditor);

var editor = /*#__PURE__*/Object.freeze({
    __proto__: null,
    get MagicHomePartyEditor () { return MagicHomePartyEditor; }
});

export { MagicHomeParty };
//# sourceMappingURL=magic-home-party.js.map
